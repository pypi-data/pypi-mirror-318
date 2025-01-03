# Social Networks
SOCIAL = [
    {"name": "Facebook", "url": "https://www.facebook.com/{}"},
    {"name": "Instagram", "url": "https://www.instagram.com/{}"},
    {"name": "X (formerly Twitter)", "url": "https://x.com/{}"},
    {"name": "LinkedIn", "url": "https://www.linkedin.com/in/{}"},
    {"name": "TikTok", "url": "https://www.tiktok.com/@{}"},
    {"name": "Threads", "url": "https://www.threads.net/@{}"},
    {"name": "Pinterest", "url": "https://www.pinterest.com/{}"},
    {"name": "Reddit", "url": "https://www.reddit.com/user/{}"},
    {"name": "Mastodon", "url": "https://{}/"},  # Instance-specific
    {"name": "Discord", "url": "https://discord.com/users/{}"},
    {"name": "Telegram", "url": "https://t.me/{}"},
    {"name": "WhatsApp", "url": "https://wa.me/{}"},
    {"name": "WeChat", "url": "https://wechat.com/{}"},
    {"name": "Signal", "url": "https://signal.me/#p/{}"},  # Updated format
    {"name": "BeReal", "url": "https://bere.al/{}"},  # Added
    {"name": "Lemon8", "url": "https://lemon8-app.com/@{}"},  # Added
    {"name": "Bluesky", "url": "https://bsky.app/profile/{}"},  # Added
    {"name": "Post", "url": "https://post.news/{}"},  # Added
    {"name": "Nostr", "url": "https://nostr.com/{}"},  # Added
    {"name": "Pebble", "url": "https://pebble.social/{}"},  # Added
]

# Developer Platforms
DEV = [
    {"name": "GitHub", "url": "https://github.com/{}"},
    {"name": "GitLab", "url": "https://gitlab.com/{}"},
    {"name": "Bitbucket", "url": "https://bitbucket.org/{}"},
    {"name": "Stack Overflow", "url": "https://stackoverflow.com/users/{}"},
    {"name": "Stack Exchange", "url": "https://stackexchange.com/users/{}"},
    {"name": "Dev.to", "url": "https://dev.to/{}"},
    {"name": "CodePen", "url": "https://codepen.io/{}"},
    {"name": "Replit", "url": "https://replit.com/@{}"},
    {"name": "Kaggle", "url": "https://www.kaggle.com/{}"},
    {"name": "HuggingFace", "url": "https://huggingface.co/{}"},
    {"name": "HackerRank", "url": "https://www.hackerrank.com/{}"},
    {"name": "LeetCode", "url": "https://leetcode.com/{}"},
    {"name": "Medium", "url": "https://medium.com/@{}"},
    {"name": "Hashnode", "url": "https://hashnode.com/@{}"},
    {"name": "Devpost", "url": "https://devpost.com/{}"},
    {"name": "Codecademy", "url": "https://www.codecademy.com/profiles/{}"},
    {"name": "Codewars", "url": "https://www.codewars.com/users/{}"},
    {"name": "Exercism", "url": "https://exercism.io/profiles/{}"},
    {"name": "TopCoder", "url": "https://www.topcoder.com/members/{}"},
    {"name": "CodeChef", "url": "https://www.codechef.com/users/{}"},
    {"name": "FreeCodeCamp", "url": "https://www.freecodecamp.org/{}"},
    {"name": "JSFiddle", "url": "https://jsfiddle.net/user/{}"},
    {"name": "NuGet", "url": "https://www.nuget.org/profiles/{}"},
    {"name": "Packagist", "url": "https://packagist.org/users/{}"},
    {"name": "PyPI", "url": "https://pypi.org/user/{}"},
    {"name": "npm", "url": "https://www.npmjs.com/~{}"},
    {"name": "Docker Hub", "url": "https://hub.docker.com/u/{}"},
    {"name": "Rust Crates.io", "url": "https://crates.io/users/{}"},
    {"name": "Go Packages", "url": "https://pkg.go.dev/{}"},  # Added
    {"name": "RubyGems", "url": "https://rubygems.org/profiles/{}"},
]

# Streaming Platforms
STREAMING = [
    {"name": "YouTube", "url": "https://www.youtube.com/{}"},
    {"name": "Twitch", "url": "https://www.twitch.tv/{}"},
    {"name": "Spotify", "url": "https://open.spotify.com/user/{}"},
    {"name": "SoundCloud", "url": "https://soundcloud.com/{}"},
    {"name": "Apple Music", "url": "https://music.apple.com/profile/{}"},
    {"name": "Deezer", "url": "https://www.deezer.com/profile/{}"},
    {"name": "Tidal", "url": "https://tidal.com/browse/user/{}"},
    {"name": "Mixcloud", "url": "https://www.mixcloud.com/{}"},
    {"name": "Pandora", "url": "https://www.pandora.com/profile/{}"},
    {"name": "Bandcamp", "url": "https://bandcamp.com/{}"},
    {"name": "Vimeo", "url": "https://vimeo.com/{}"},
    {"name": "Dailymotion", "url": "https://www.dailymotion.com/{}"},
    {"name": "Rumble", "url": "https://rumble.com/user/{}"},
    {"name": "LiveLeak", "url": "https://www.liveleak.com/user/{}"},
    {"name": "Metacafe", "url": "https://www.metacafe.com/channels/{}"},
    {"name": "BitChute", "url": "https://www.bitchute.com/channel/{}"},
    {"name": "DTube", "url": "https://d.tube/#!/c/{}"},
    {"name": "Streamable", "url": "https://streamable.com/{}"},
    {"name": "Caffeine", "url": "https://www.caffeine.tv/{}"},
    {"name": "Smashcast", "url": "https://www.smashcast.tv/{}"},
    {"name": "DLive", "url": "https://dlive.tv/{}"},
    {"name": "Periscope", "url": "https://www.pscp.tv/{}"},
    {"name": "YouTube Gaming", "url": "https://gaming.youtube.com/channel/{}"},
    {"name": "Facebook Gaming", "url": "https://www.facebook.com/gaming/{}"},
    {"name": "Trovo", "url": "https://trovo.live/{}"},
    {"name": "OnlyFans", "url": "https://onlyfans.com/{}"},
    {"name": "Fansly", "url": "https://fansly.com/{}"},
    {"name": "Buy Me a Coffee", "url": "https://www.buymeacoffee.com/{}"},
]

# Gaming Platforms
GAMING = [
    {"name": "Steam", "url": "https://steamcommunity.com/id/{}"},
    {"name": "Epic Games", "url": "https://www.epicgames.com/account/{}"},
    {"name": "Xbox Live", "url": "https://account.xbox.com/profile?gamertag={}"},
    {"name": "PlayStation Network", "url": "https://my.playstation.com/profile/{}"},
    {"name": "Origin (EA)", "url": "https://www.origin.com/usa/en-us/profile/{}"},
    {"name": "Ubisoft Connect", "url": "https://connect.ubisoft.com/profile/{}"},
    {"name": "GOG", "url": "https://www.gog.com/u/{}"},
    {"name": "Roblox", "url": "https://www.roblox.com/user.aspx?username={}"},
    {"name": "Minecraft", "url": "https://minecraft.net/en-us/profile/{}"},
    {"name": "Fortnite", "url": "https://fortnite.com/player/{}"},
    {"name": "Battle.net", "url": "https://battle.net/account/management/{}"},
    {"name": "Faceit", "url": "https://www.faceit.com/en/players/{}"},
    {"name": "Smash.gg", "url": "https://smash.gg/{}"},
    {"name": "Nintendo Switch", "url": "https://www.nintendo.com/{}"},
    {"name": "Speedrun.com", "url": "https://www.speedrun.com/user/{}"},
    {"name": "Kongregate", "url": "https://www.kongregate.com/accounts/{}"},
    {"name": "Newgrounds", "url": "https://{}.newgrounds.com"},
    {"name": "Itch.io", "url": "https://{}.itch.io"},
    {"name": "GameJolt", "url": "https://gamejolt.com/@{}"},
    {"name": "Steam Workshop", "url": "https://steamcommunity.com/id/{}/myworkshopfiles/"},
    {"name": "CurseForge", "url": "https://www.curseforge.com/members/{}"},
    {"name": "Mod DB", "url": "https://www.moddb.com/members/{}"},
    {"name": "Indie DB", "url": "https://www.indiedb.com/members/{}"},
    {"name": "GameBanana", "url": "https://gamebanana.com/members/{}"},
    {"name": "Humble Bundle", "url": "https://www.humblebundle.com/user/{}"},
    {"name": "G2A", "url": "https://www.g2a.com/{}"},
    {"name": "Green Man Gaming", "url": "https://www.greenmangaming.com/{}"},
    {"name": "Epic Games Store", "url": "https://www.epicgames.com/store/en-US/account/{}"},
]

# Forums & Communities
FORUMS = [
    {"name": "Quora", "url": "https://www.quora.com/profile/{}"},
    {"name": "4chan", "url": "https://boards.4chan.org/{}"},
    {"name": "9GAG", "url": "https://9gag.com/u/{}"},
    {"name": "Imgur", "url": "https://imgur.com/user/{}"},
    {"name": "Flickr", "url": "https://www.flickr.com/people/{}"},
    {"name": "DeviantArt", "url": "https://{}.deviantart.com"},
    {"name": "Behance", "url": "https://www.behance.net/{}"},
    {"name": "Dribbble", "url": "https://dribbble.com/{}"},
    {"name": "ArtStation", "url": "https://www.artstation.com/{}"},
    {"name": "Goodreads", "url": "https://www.goodreads.com/{}"},
    {"name": "Letterboxd", "url": "https://letterboxd.com/{}"},
    {"name": "MyAnimeList", "url": "https://myanimelist.net/profile/{}"},
    {"name": "Gaia Online", "url": "https://www.gaiaonline.com/profiles/{}"},
    {"name": "Wattpad", "url": "https://www.wattpad.com/user/{}"},
    {"name": "Fanfiction.net", "url": "https://www.fanfiction.net/u/{}"},
    {"name": "Archive of Our Own", "url": "https://archiveofourown.org/users/{}"},
]

# Other Platforms
OTHER = [
    {"name": "Substack", "url": "https://{}.substack.com"},
    {"name": "Google (Profile)", "url": "https://profiles.google.com/{}"},
    {"name": "Microsoft (Profile)", "url": "https://account.microsoft.com/profile/{}"},
    {"name": "Apple ID", "url": "https://appleid.apple.com/account/{}"},
    {"name": "Slack", "url": "https://{}.slack.com"},
    {"name": "Trello", "url": "https://trello.com/{}"},
    {"name": "Notion", "url": "https://www.notion.so/{}"},
    {"name": "Airtable", "url": "https://airtable.com/{}"},
    {"name": "Zoom", "url": "https://zoom.us/profile/{}"},
    {"name": "Skype", "url": "https://www.skype.com/{}"},
    {"name": "WordPress.com", "url": "https://{}.wordpress.com"},
    {"name": "Blogger", "url": "https://www.blogger.com/profile/{}"},
    {"name": "Wix", "url": "https://{}.wixsite.com"},
    {"name": "Squarespace", "url": "https://{}.squarespace.com"},
    {"name": "Weebly", "url": "https://{}.weebly.com"},
    {"name": "Ghost", "url": "https://{}.ghost.io"},
    {"name": "Medium", "url": "https://medium.com/@{}"},
    {"name": "Tumblr", "url": "https://{}.tumblr.com"},
    {"name": "LiveJournal", "url": "https://{}.livejournal.com"},
    {"name": "Blogspot", "url": "https://{}.blogspot.com"},
]

PAYMENT = [
    {"name": "PayPal", "url": "https://paypal.me/{}"},
    {"name": "Venmo", "url": "https://venmo.com/{}"},
    {"name": "Cash App", "url": "https://cash.app/${}"},
    {"name": "Stripe", "url": "https://stripe.com/{}"},
    {"name": "Web3 Wallet (ETH)", "url": "https://etherscan.io/address/{}"},
    {"name": "Web3 Wallet (BTC)", "url": "https://blockchair.com/bitcoin/address/{}"},
    {"name": "Solana", "url": "https://explorer.solana.com/address/{}"},
    {"name": "Linktree", "url": "https://linktr.ee/{}"},  # Added
    {"name": "Beacons", "url": "https://beacons.ai/{}"},  # Added
    {"name": "Bio.link", "url": "https://bio.link/{}"},  # Added
]

PRO = [
     {"name": "Fiverr", "url": "https://www.fiverr.com/{}"},
    {"name": "Upwork", "url": "https://www.upwork.com/freelancers/~{}"},
    {"name": "Behance", "url": "https://www.behance.net/{}"},
    {"name": "Dribbble", "url": "https://dribbble.com/{}"},
    {"name": "ArtStation", "url": "https://www.artstation.com/{}"},
    {"name": "Gumroad", "url": "https://gumroad.com/{}"},
    {"name": "Shopify", "url": "https://{}.myshopify.com"},
    {"name": "Etsy", "url": "https://www.etsy.com/shop/{}"},
    {"name": "Product Hunt", "url": "https://www.producthunt.com/@{}"},
    {"name": "Patreon", "url": "https://www.patreon.com/{}"},
    {"name": "Kickstarter", "url": "https://www.kickstarter.com/profile/{}"},
    {"name": "Indiegogo", "url": "https://www.indiegogo.com/individuals/{}"},
    {"name": "GoFundMe", "url": "https://www.gofundme.com/f/{}"},
]
