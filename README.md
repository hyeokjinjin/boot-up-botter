# boot-up-botter
Discord Bot to "boot up" people in a server

## Commands
- `$bootup @user`
  - Spams five mentions in the channel where command was send and additionally sends a private direct message to the user that is being boot up.
  - Has the ability to "bootup" multiple users as well.
  - i.e. `$bootup @luhve` or `$bootup @luhve @gurwls`

- `$bootup @user @time @units`
  - Same functionality as the `$bootup` command, but adds a delay for inputted amount of time to "bootup" a user in a specific time.
  - i.e. `$bootup @luhve 10 minutes` or `$bootup @luhve @gurwls 2 hours`
