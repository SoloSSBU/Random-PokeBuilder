# Random-PokeBuilder

This app takes a list of your favorite pokemon, randomizes them, and then picks a team in which only one of each type is allowed. 
After picking the team, the app goes online to smogon (a website with the most popular pokemon builds) using selenium, 
and copy's the most popular build for each pokemon in the team to your clipboard. Then simply paste the team into Pokemon Showdown and play!

## Why I made this app

My brother and I were bored one day and decided to play some pokemon random battles on Pokemon Showdown. Once we started playing we realized that
we just weren't fond of the Pokemon we were getting and decided it would be a lot more fun if we could do random battles with only our favorite
pokemon. At first we did this manually by writing out all our favorites, assigning them numbers, and using an online random number generator.
We noticed the teams we were getting weren't very typing balanced. Far too often one of us would end up with 3 of the same type and get swept
by a singular counter from the other side. With the addition of a new rule that each team could only have a max of 1 of each type, we started
rerolling duplicates. Needless to say this process was beginning to take far too long, and I haven't even mentioned the fact that we were
building the stats, items, movesets, and abilities of all these Pokemon. At a certain point we just started looking up common builds and just
changing a few import things to match the team.

While this app does take a second to pull up the smogon pages and wait for ad to pop up and close it so that it can copy the builds, it saved
my brother and I at least 10 minutes each time we used it.
