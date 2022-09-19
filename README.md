July 2022 Computer Sciences: Programming (CIS1048-N) by Teesside University

Worksheet 8 Networking Programming

[ASSESSMENT] Question 3: Modifying home_brew.py (my_home_brew.py)
The Punk API takes Brewdog's DIY Dog and turns it into a searchable, filterable API that's completely free and open source. Documentation for the API is available at:
	https://punkapi.com/documentation/v2   
The file home_brew.py is available on Blackboard (1st demo). Download the file and run. Read through the API documentation, and step through each statement, if you are unsure on any statements speak to your module tutor.
https://api.punkapi.com/v2/beers gets beers from the Punk API. You can apply filters using URL parameters, the available options are listed over page:
```
PARAM	TYPE	DETAILS
abv_gt	number	Returns all beers with ABV greater than the supplied number
abv_lt	number	Returns all beers with ABV less than the supplied number
ibu_gt	number	Returns all beers with IBU greater than the supplied number
ibu_lt	number	Returns all beers with IBU less than the supplied number
ebc_gt	number	Returns all beers with EBC greater than the supplied number
ebc_lt	number	Returns all beers with EBC less than the supplied number
beer_name	string	Returns all beers matching the supplied name (this will match partial strings as well so e.g punk will return Punk IPA), if you need to add spaces just add an underscore (_).
yeast	string	Returns all beers matching the supplied yeast name, this performs a fuzzy match, if you need to add spaces just add an underscore (_).
brewed_before	date	Returns all beers brewed before this date, the date format is mm-yyyy e.g 10-2011
brewed_after	date	Returns all beers brewed after this date, the date format is mm-yyyy e.g 10-2011
hops	string	Returns all beers matching the supplied hops name, this performs a fuzzy match, if you need to add spaces just add an underscore (_).
malt	string	Returns all beers matching the supplied malt name, this performs a fuzzy match, if you need to add spaces just add an underscore (_).
food	string	Returns all beers matching the supplied food string, this performs a fuzzy match, if you need to add spaces just add an underscore (_).
ids	string (id|id|...)	Returns all beers matching the supplied ID's. You can pass in multiple ID's by separating them with a | symbol.
```

Save a copy of home_brew.py as my_home_brew.py. Modify the payload dictionary values before making the request. 
payload = { 'abv_gt':5, 'brewed_after':'12-2015' }

1.	Choose combinations of different parameters from the table above to return different beers. 
2.	Why not try a fuzzy match on food or beer_name?
3.	Leave comments in your code highlighting the changes you have made.

----------------------------------------
Lecturer's comment:
Very good
