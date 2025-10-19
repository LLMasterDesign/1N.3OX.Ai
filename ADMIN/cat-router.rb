#!/usr/bin/env ruby
# CAT-ROUTER - Category Management (Ruby)
# Version: 1.0

require 'fileutils'
require 'time'

CAT_FOLDERS = [
  "(CAT.1) Self",
  "(CAT.2) Education",
  "(CAT.3) Business",
  "(CAT.4) Family",
  "(CAT.5) Social"
]

def show_dashboard
  puts "\n  CAT ROUTER DASHBOARD"
  puts "  ===================="
  puts ""
  
  CAT_FOLDERS.each do |cat|
    if Dir.exist?(cat)
      inbox_path = File.join(cat, "1N.3OX")
      if Dir.exist?(inbox_path)
        item_count = Dir.glob(File.join(inbox_path, "*")).length
        if item_count > 0
          puts "  #{cat} - #{item_count} items"
        else
          puts "  #{cat} - Empty"
        end
      end
    end
  end
  
  puts ""
  puts "  Commands: ruby cat-router.rb [dashboard|showall|route]"
  puts ""
end

def show_all
  puts "\n  ALL ITEMS"
  puts "  ========="
  puts ""
  
  total_items = 0
  
  CAT_FOLDERS.each do |cat|
    if Dir.exist?(cat)
      inbox_path = File.join(cat, "1N.3OX")
      if Dir.exist?(inbox_path)
        items = Dir.glob(File.join(inbox_path, "*"))
        if items.any?
          puts "  #{cat} - #{items.length} items"
          items.each { |item| puts "    - #{File.basename(item)}" }
          puts ""
          total_items += items.length
        end
      end
    end
  end
  
  puts "  Total: #{total_items} items"
  puts ""
end

def route_item(item_path, target_category)
  unless File.exist?(item_path)
    puts "  ERROR: Item not found: #{item_path}"
    return
  end
  
  target_inbox = File.join(target_category, "1N.3OX")
  unless Dir.exist?(target_inbox)
    puts "  ERROR: Category not found: #{target_category}"
    return
  end
  
  filename = File.basename(item_path)
  destination = File.join(target_inbox, filename)
  
  FileUtils.mv(item_path, destination)
  
  # Log to category
  log_path = File.join(target_category, ".3ox", "3ox.log")
  timestamp = Time.now.strftime("%Y-%m-%d %H:%M:%S")
  log_entry = "\n[#{timestamp}] ROUTED: #{filename}"
  
  File.open(log_path, 'a') { |f| f.write(log_entry) }
  
  puts "  SUCCESS: #{filename} -> #{target_category}"
end

def show_help
  puts <<~HELP
  
  CAT-ROUTER Commands:
  ====================
  
  ruby cat-router.rb dashboard
    View status of all categories
  
  ruby cat-router.rb showall
    List all items in all categories
  
  ruby cat-router.rb route <file> <category>
    Route item to specific category
    
  Example:
    ruby cat-router.rb route invoice.pdf "(CAT.3) Business"
  HELP
end

# Main
action = ARGV[0]&.downcase

case action
when "dashboard"
  show_dashboard
when "showall"
  show_all
when "route"
  if ARGV.length >= 3
    route_item(ARGV[1], ARGV[2])
  else
    show_help
  end
else
  show_help
end

