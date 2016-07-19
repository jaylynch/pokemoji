![Pokemoji](https://github.com/jaylynch/pokemoji/raw/master/img/logo.png)
# pokemoji

Pokemon emoji list for [emojipacks](https://github.com/lambtron/emojipacks)

Easily import all of the original 151 Pokemon to your Slack team!

Many thanks to [PokemonGo-Map](https://github.com/AHAAAAAAA/PokemonGo-Map/blob/master/LICENSE) and [Pokéapi](https://pokeapi.co/).

# TLDR

https://raw.githubusercontent.com/jaylynch/pokemoji/master/pokemon-by-name.yaml

# Install

- Have [Node.js](https://nodejs.org/)

- Install [emojipacks](https://github.com/lambtron/emojipacks) and run it on the list file https://raw.githubusercontent.com/jaylynch/pokemoji/master/pokemon-by-name.yaml:
  ```
  $ npm install -g emojipacks
  ...

  $ emojipacks
  Slack subdomain: yourcompanyname
  Email address login: your.fancyname@yourcompanyname.com
  Password: *********
  Path or URL of Emoji yaml file: https://raw.githubusercontent.com/jaylynch/pokemoji/master/pokemon-by-name.yaml
  ```

- Wait a while... 🚶☕😴💃📖

- Paste `test-by-name` or `test-by-number` into a DM with slackbot and see if it worked!

# Options

- Use `pokemon-by-name.yaml` for the emoji to be added by name (eg. `:bulbasaur:`, `:psyduck:`)
- Use `pokemon-by-number.yaml` for the emoji to be added by number (eg. `:pokemon-1:`, `:pokemon-54:`)


# Misc

The script which generated the `-by-name` file from the numbers is attached for curiosity's sake. I'd suggest avoiding it, it was _very_ hastily slapped together, but if you really want to just `npm install && npm run gen-name-yaml`

`gen1.json` and `gen1.yaml` contain the raw data from Pokéapi in case you want to muck about with it.

`test-by-name` and `test-by-number` contain the full list, in order, as Slack emoji ready to copy-paste into a channel to test them.

# License

Code is MIT. Go bananas~ 🍌🍌🍌🍌🍌

(Copyright on actual Pokemon imagery and data may be a very different story - use your own judgement there, ❤️ Nintendo)
