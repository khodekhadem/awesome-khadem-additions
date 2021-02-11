local wibox = require("wibox")
local awful = require("awful")
local naughty = require("naughty")
local watch = require("awful.widget.watch")

--local path_to_icons = "/usr/share/icons/Arc/actions/22/"
local path_to_icons = "/home/eby/.config/awesome/km-adition/icons/22"

local bb = 55

local clock = os.clock
function mysleep(n)  -- seconds
  local t0 = clock()
  while clock() - t0 <= n do end
end

email_widget = wibox.widget.textbox()
email_widget:set_font('Play 9')

email_icon = wibox.widget.imagebox()
email_icon:set_image(path_to_icons .. "/mail-mark-new.png")

watch(
    --"python /home/eby/.config/awesome/email-widget/count_unread_emails.py", 20, 
    "acpi", 90, 
   function(widget, stdout, stderr, exitreason, exitcode)
        local unread_emails_num = bb
        if (unread_emails_num > 0) then
        	local handle = io.popen('acpi')
  		local result = handle:read("*a")
		handle:close()
		io.popen("python3 ~/.config/awesome/km-adition/charge-allert/b.py")
		--email_icon:set_image(path_to_icons .. "/go-home.png")
		email_icon:set_image(path_to_icons .. "/dialog-warning.png")
	        email_widget:set_text(result)
        end	
    end
)


function show_status()
    awful.spawn.easy_async([[bash -c 'python3 ~/.config/awesome/km-adition/widgets/kyco.py']],
        function(stdout, stderr, reason, exit_code)   
                --local handle = io.popen('xrandr --prop --verbose | grep -A10 " connected" | grep "Brightness"')
                --local result = handle:read("*a")
                --handle:close()
            naughty.notify{
                text = '<span  size="xx-large">'.. stdout ..'</span>',
                timeout = 5, hover_timeout = 0.5,
                width = 400,
            }
        end
    )
end

email_icon:connect_signal(
"mouse::enter",
function() show_status()
end)
