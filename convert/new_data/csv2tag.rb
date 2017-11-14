require_relative 'CameraRollTag.rb'
require 'json'

require 'fastimage'
require 'csv'

def get_image_size(path)
  raise "File #{path} not exist!" unless File.exist?(path)
  FastImage.size(path)
end 

DATA = CSV.read('./tag_utf8.csv')[1..-1]

def gen_data(sample=true)
  if sample
    @data = DATA[1..1]
  else
    @data = DATA
  end
  nil
end

def filename(path)
  path.split('\\').last
end

def name2size(filename)
  get_image_size "./安全帽使用场景/#{filename}"  
end

def process(line, debug=false)
  data = line.compact
  index = data[0]
  name = filename(data[1])
  width, height = name2size(name)
  boxes = []
  data[2..-1].each_slice(2).with_index { |(tl, br), i| 
    puts "#{i} - #{tl}, #{br}" if debug
    type = (i % 2 == 1) ? 'human' : 'helmet'
    xi, yi = tl.split(',').map(&:to_i) 
    xm, ym = br.split(',').map(&:to_i)
    xmin, xmax = [xi, xm].sort
    ymin, ymax = [yi, ym].sort
    puts "#{type} - #{xmin} #{ymin} #{xmax} #{ymax}" if debug
    boxes << {
      :class => type, 
      :xmin => xmin/width.to_f, 
      :ymin => ymin/height.to_f, 
      :xmax => xmax/width.to_f, 
      :ymax => ymax/height.to_f
    }
  }

  puts "#{name}, [#{width}, #{height}], #{boxes}" if debug
  [name, {:boxes => boxes}]
end

def extract(debug=false)
  @data.map{|x| process(x, debug)}.to_h
end

def valid
  check = @result.map{|k,v| v[:boxes].map{|y| y[:index] = k; y}}.flatten
  invalid = check.select {|h| (h[:xmin] > h[:xmax]) || (h[:ymin] > h[:ymax])}
  raise "check failed #{invalid}" if invalid.length != 0
end

def run(debug=false)
  gen_data(false)
  @result=extract(false)
  File.open("./CameraRollTag.json","w") do |f|
    f.write(@result.to_json)
  end
end

