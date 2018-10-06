# rolldie.live
This is the source code for rolldie.live, a simple cURL-able dice rolling utility!

## Usage
Check out the basic instructions by simply running:
`curl rolldie.live`

## Normal rolling
Requesting something simple like 1d20 will output like so:

```
curl rolldie.live/1d20
3
```

## Output format options
The following formats are available:

json
```
curl rolldie.live/20d20/json
[1, 15, 8, 10, 19, 1, 9, 10, 16, 7, 4, 4, 15, 20, 3, 11, 9, 10, 8, 13]
```

csv
```
curl rolldie.live/20d20/csv
16,1,14,15,20,2,11,16,4,13,2,5,5,19,3,8,14,20,16,7
```

raw
```
curl rolldie.live/20d20/raw
13 12 16 16 16 8 20 1 8 5 6 8 10 18 7 9 4 10 12 17
```
