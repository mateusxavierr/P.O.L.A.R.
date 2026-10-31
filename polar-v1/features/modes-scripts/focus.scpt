tell application "Finder"
	set screenBounds to bounds of window of desktop
end tell

set screenWidth to item 3 of screenBounds
set screenHeight to item 4 of screenBounds

set vsWidth to screenWidth / 1.7
set halfHeight to screenHeight / 2
set notionChatWidth to screenWidth - vsWidth
set chatPositionHeight to screenHeight / 4.6
set chatHeight to screenHeight - chatPositionHeight

-- Open the apps
tell application "Visual Studio Code" to activate
tell application "Notion" to activate
tell application "ChatGPT" to activate


-- Position Visual Studio Code on the left (half of the screen)
tell application "System Events"
	tell process "Electron"
		if (count of windows) > 0 then
			set frontmost to true
			set position of front window to {0, 0}
			set size of front window to {vsWidth, screenHeight}
		end if
	end tell
end tell

-- Position Notion on the top right
tell application "System Events"
	tell process "Notion"
		if (count of windows) > 0 then
			set frontmost to true
			set position of front window to {vsWidth, 0}
			set size of front window to {notionChatWidth, halfHeight}
		end if
	end tell
end tell

-- Position ChatGPT on the bottom right
tell application "System Events"
	tell process "ChatGPT"
		if (count of windows) > 0 then
			set frontmost to true
			set position of front window to {vsWidth, chatPositionHeight}
			set size of front window to {notionChatWidth, chatHeight}
		end if
	end tell
end tell