# Coal Haul changelog

Version numbers: every push to git adds 1 to the last number (0.1.0 → 0.1.1 → … → 0.1.10 → 0.1.100). The middle number changes only when we decide on a big step. 1.0.0 is the first release.

Saves remember the version they were made with. In multiplayer, players must be on the same version: a player on another version is turned away and asked to reload the page.

## 0.1.3 · 18 Nov 2026
- Added: saves work across versions. A save is brought up to date when loaded; damaged parts and things the game no longer has are left out instead of breaking the load
- Added: a save from a newer version loads with a warning and is marked in the save list; if a save cannot be loaded, a new map starts and the save stays untouched
- Fixed: saves from 0.1.1 on the bigger power plant: anything that now stands inside a building is moved just outside its nearest wall

## 0.1.2 · 18 Nov 2026
- Fixed: lag on big screens. The streets were drawn from scratch every frame; they are now painted once into the cached ground and only repainted when a street changes
- Changed: the power plant is 14 x 14 squares, centred on the middle chunk of its lot, with a roof laid out for the square shape; its room inside is 14 x 14 too
- Changed: the buildings' readout boards are hidden for now, while the buildings are reworked
- Added: a players list kept with the save. /players opens a window of everyone who has been on the map, where the host can kick, ban or remove a player
- Fixed: a player who joins again no longer gets another starting pickup; they come back on foot where they left
- Added: other players' names above them, also while they drive, drawn over roofs and in the dark
- Added: hovering a vehicle's seats shows the other players sitting in them

## 0.1.1 · 18 Nov 2026
- Fixed: static in the sound. The looping noise behind the wind, engines and machines clicked every time it went round; it now loops seamlessly
- Changed: wind darker and quieter; door, starter and engine stop with less hiss
- Fixed: lag from sound. Sound settings are only sent to the audio when they change, and sounds at rest are switched off until needed

## 0.1.0 · 18 Nov 2026
Version numbering starts here, with everything built so far:
- Hauling coal and building the chain of buildings, on a top-down map with thick coloured walls on every lot
- Vehicles: truck and semi, dump truck, flatbed, crane (with cab view, tools and feet), forklift; traffic barriers
- Day (15 minutes) and night (5 minutes); lights on L, white reversing lamps, crane hook work light
- Camera views on TAB; minimap with optional coordinates
- Main menu, Esc menu, settings (controls, sound channels, touch), saves with names and pictures in the browser's database
- Multiplayer by 5-letter code, chat with commands
- Sounds, all made by the game's own code (no recordings): an engine for each vehicle (diesels, petrol car, ATV, forklift), engine start and stop, low fuel and out of fuel, bumps and crashes, brakes and air brakes, footsteps, off-road rumble, reversing beeper, horn on H, lights on and off, crane hydraulics and tools, hitching, lifting, winching, dumping, buildings at work, wind, birds, crickets, dusk and dawn, building and demolishing, money, goals, saving, players joining and leaving, quiet music
- PC first, phones supported (joystick where you touch, button arc)
