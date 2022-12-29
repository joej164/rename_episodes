from pathlib import Path

TESTING = True

base_path = "C:\media\Shows\Star Trek Voyager (1995) [tvdbid-74550]"
SEASON = 7

season = Path(base_path) / f"Season {SEASON:02d}"

MIN_SIZE_OF_EPISODE = 1000000000 
EPISODE_BASE = f"Episode S{SEASON:02d}E"
episode_count = 1

if TESTING:
    print("Testing Mode!!!")
else:
    print("Move Mode")

for item in season.iterdir():
    if item.is_dir():
        for i in item.iterdir():
            if i.suffix == ".mkv" and i.stat().st_size > 2 * MIN_SIZE_OF_EPISODE:
                new_name = f"{EPISODE_BASE}{episode_count:02d}-E{episode_count + 1:02d}"
                episode_count += 2
            elif i.suffix == ".mkv" and i.stat().st_size > MIN_SIZE_OF_EPISODE:
                new_name = f"{EPISODE_BASE}{episode_count:02d}"
                episode_count += 1
            else:
                continue

            print(i, i.stat().st_size, new_name)
            new_dir = i.parent.parent
            new_file = new_dir / f"{new_name}.mkv"
            if new_file.exists():
                raise FileExistsError("The file already exists")

            if not TESTING:
                # Code to rename and move the file
                i.rename(new_file)
                print(f"New File and Location: {new_file}")
                pass
            else:
                # What could have been
                print(f"TESTING: New File and Location: {new_file}")
