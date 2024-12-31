# lockdown_protocol_extra_bot

**ABANDONED**.
 
Let u to add some extra challenges for players of lockdown protocol with telegram bot.

# Installation and start

``` bash
pip install --upgrade pip
pip3 install lockdown_protocol_extra_bot
```

Then create file `settings.json` with content:

``` json
{
    "telegram-config": {
        "token": "{YOUR_TELEGRAM_TOKEN}",
        "password": "{YOUR_PASSWORD}"
    }
}
```

You can get token from `@BotFather` (it is telegram bot). With `{YOUR_PASSWORD}` you can restart bot. Only with this password bot can be restarted from telegram chat.

And run:

``` bash
lockdown_protocol_extra_bot start settings.json
```

# Adding your challanges

Just change file `./lockdown_protocol_extra_bot/gen_challenges.py` (add yours to function `get_challenges`). Or `venv/lib64/pythonX.XX/site-packages/lockdown_protocol_extra_bot/gen_challenges.py` if installed from `pip`.
