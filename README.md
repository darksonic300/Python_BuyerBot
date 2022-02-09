# Introduction

This is my first Python real project. It's a bot that simply opens N instances of the Brave browser to a linked item on Amazon and buys it automatically.
If a user is not logged in, it will automatically fill the credentials and buy the item.

# How it works

After defining the chromedriver.exe and referring to Brave path, through a "cred.txt" file it will read the first line as the link to the item the user wants to buy.
It will also read th 2nd and 3rd line as email and password for login.
It will open NUM instances (defined like a constant in the code) of the browser to that link, and if the user is not logged in the credentials will be filled
automatically by the bot.
Finally, the item will be bought and the instance closed.

# What do I want it to be

I would like this bot to become more efficient, and maybe work on other sites than just Amazon.
I plan on introducing an Anti-Captcha method in the future, and see where I can push it.
