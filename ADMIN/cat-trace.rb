#!/usr/bin/env ruby
# CAT-TRACE - Category Trace System (Ruby)
# Version: 1.0

require 'yaml'
require 'time'

def get_categories
  Dir.glob("(CAT.*").select { |f| File.directory?(f) }.sort
end

def scrape_logs(category_path)
  logfile = File.join(category_path, '.3ox', '3ox.log')
  return [] unless File.exist?(logfile)
  
  receipts = []
  File.readlines(logfile, encoding: 'utf-8').each do |line|
    if line.match?(/ROUTED:|COMPLETE|SUCCESS/)
      receipts << line.strip
    end
  end
  receipts
rescue => e
  puts "    ERROR reading log: #{e}"
  []
end

def generate_report
  categories = get_categories
  
  puts "\n  CAT-TRACE REPORT"
  puts "  ================"
  puts "\n  Timestamp: #{Time.now.strftime('%Y-%m-%d %H:%M:%S')}"
  puts "  Categories: #{categories.length}"
  puts
  
  total_receipts = 0
  categories.each do |cat|
    receipts = scrape_logs(cat)
    total_receipts += receipts.length
    
    if receipts.any?
      puts "  #{cat} - #{receipts.length} receipts"
      receipts.take(3).each { |r| puts "    • #{r[0..60]}..." }
      puts "    ... and #{receipts.length - 3} more" if receipts.length > 3
    else
      puts "  #{cat} - No activity"
    end
  end
  
  puts "\n  Total receipts: #{total_receipts}"
  puts
end

def batch_receipts
  categories = get_categories
  
  timestamp = Time.now.strftime('%Y%m%d-%H%M%S')
  batch_file = "receipts-batch-#{timestamp}.yaml"
  
  puts "\n  Batching receipts to: #{batch_file}"
  
  File.open(batch_file, 'w', encoding: 'utf-8') do |out|
    out.puts "# Receipt Batch - #{Time.now.strftime('%Y-%m-%d %H:%M:%S')}"
    out.puts "# Categories: #{categories.length}\n\n"
    
    categories.each do |cat|
      receipts = scrape_logs(cat)
      if receipts.any?
        out.puts "## #{cat}"
        out.puts "receipts: #{receipts.length}"
        receipts.each { |r| out.puts "  - #{r}" }
        out.puts "\n"
      end
    end
  end
  
  total = categories.sum { |c| scrape_logs(c).length }
  puts "  ✓ Batched #{total} receipts"
  puts
end

def show_help
  puts <<~HELP
  
  CAT-TRACE Commands (Ruby):
  ==========================
  
  ruby cat-trace.rb report
    Generate trace report from all 3ox.log files
  
  ruby cat-trace.rb batch
    Batch all receipts into single file
  
  ruby cat-trace.rb help
    Show this help
  HELP
end

# Main
action = ARGV[0]&.downcase

case action
when 'report'
  generate_report
when 'batch'
  batch_receipts
when 'help'
  show_help
else
  show_help
end

