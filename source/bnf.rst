
BNF: Backus Naur Formal
============================

BNF stands for **Backus Naur Formal**, which is a notation technique to describe **context-free grammars** [wikibnf]_ [wikicfg]_. 

Background
==============

#. We use programming languages to write programs.
#. We use grammars to describe programming languages.
#. We use notations to describe grammars.
#. We implement grammars as automata.
#. We use automata to recognize programming languages.

Types of Grammars
--------------------

Different grammars have different abilities of describing languages. According to Chomsky [wikich]_, there are four types of grammars in descending order w.r.t. their abilities.

Type 0
	Unrestricted grammars.

Type 1
	Context-sensitive grammars.

Type 2
	Context-free grammars.

Type 3
	Regular grammars.

These grammars correspond to different type of languages, and they use different notations to describe themselves. BNF is one of the notations that can describe context-free grammars.

BNF in Action
=================

.. productionlist::
	postal-address	: `name-part` street-address zip-part
	name-part 		: personal-part last-name opt-suffix-part
					: | personal-part name-part
	personal-part 	: first-name 
					: | initial "." 
	opt-suffix-part : "Sr." | "Jr." | roman-numeral | ""
	street-address 	: house-num street-name opt-apt-num
	zip-part		: town-name "," state-code zip-code
	opt-apt-num		: apt-num | ""

.. note:: This example is taken from Wikipedia [wikibnf]_



.. [wikibnf] https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form
.. [wikicfg] http://en.wikipedia.org/wiki/Context-free_grammar
.. [wikich] http://en.wikipedia.org/wiki/Chomsky_hierarchy
