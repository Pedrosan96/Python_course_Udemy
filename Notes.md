- Itereator gives a useful way to iterate in a cleaner way
	- Is an obect that allows to traverse through the elements os a
collection.
	- It is compened of:
		- Iter method: Returns itself
		- Next method: Retuens the next value
- Generator is function that produces a sequence of results rather than a single
  value. Generators are iterators, a kind of iterable you can only iterate over
 once. Generators do not store all the values in memory, they generate the values 
on the fly.[Goog explanation](https://stackoverflow.com/questions/231767/what-does-the-yield-keyword-do)
	yield: This is a key word that returns the next value until there is
one.

- Regular expressions are sequences of characters that forms a searchable
  pattern. This can contain ordinary characters (a-z, A-Z, 0-9) and spetial
chacaters as:
	- ".": Matches any characters except New line.
	- "^": Matches the start of a string.
	- "$": Matches the end of a string or just before the new one.
	- "\*": Matches 0 or more repetitions of a preceding Regular
	  Expressions(RE).
	- "+": Matches 1 or more repetitions of preceding RE.
	- "?": Matches 0 or 1 repetitions of preceding RE.
	- "{m}": Copies the "m" number of times of the preceding RE.
	- "{m,n}: Matches from "m" to "n" repetitions of preceding RE.

