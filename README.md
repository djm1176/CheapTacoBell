
# Cheap Taco Bell

Gets you a categorized list of items on Taco Bell's menu, sorted by **calories per US dollar**.


## Features

- Very Lightweight
- Updates as Taco Bell's Menu Changes
- Caches Menu to Disk
- Groups Menu Items by Category

Cheap Taco Bell sorts every item on Taco Bell's menu by its amount of calories per US dollar ($). Therefore, if you're wanting to get the most bang for your buck, regardless of nutrition (We're talking about Taco Bell here, not the farmer's market), simply run the script and see which item has the highest value!
## Running

Clone the project

```bash
  git clone https://github.com/djm1176/CheapTacoBell.git
```

Navigate to the project

```bash
  cd ./CheapTacoBell
```

Install dependencies

```bash
  pip install -r requirements.txt
```

Run the script

```bash
  python -m main
```


## Roadmap

- [ ]  More sorting options and nutritional info
- [ ]  Command line options
- [x]  Expire the cached menu after a fixed period of time
  - Menu now expires after 3 days
- [ ]  Color coding might be cool
- [ ]  Properly tabulate the list
- [ ]  Generate a recommended purchase list by priority
  - [ ]  Allow user to enter in priority choice (most calories; healthiest; most protein; least sodium)
  - [ ]  Allow user to enter in meal budget
  - [ ]  Estimate sales tax by provided zip code
