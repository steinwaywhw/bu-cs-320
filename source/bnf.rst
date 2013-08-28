
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
	postal_address	: `name_part` `street_address` `zip_part`
	name_part 		: `personal_part` `last_name` `opt_suffix_part`
					: | `personal_part` `name_part`
	personal_part 	: `first_name`
					: | `initial` "." 
	opt_suffix_part : "Sr." | "Jr." | `roman_numeral` | ""
	street_address 	: `house_num` `street_name` `opt_apt_num`
	zip_part		: `town_name` "," `state_code` `zip_code`
	opt_apt_num		: `apt_num` | ""

.. note:: This example is taken from Wikipedia [wikibnf]_

.. productionlist::
   try_stmt: try1_stmt | try2_stmt
   try1_stmt: "try" ":" `suite`
            : ("except" [`expression` ["," `target`]] ":" `suite`)+
            : ["else" ":" `suite`]
            : ["finally" ":" `suite`]
   try2_stmt: "try" ":" `suite`
            : "finally" ":" `suite`



.. [wikibnf] https://en.wikipedia.org/wiki/Backus%E2%80%93Naur_Form
.. [wikicfg] http://en.wikipedia.org/wiki/Context-free_grammar
.. [wikich] http://en.wikipedia.org/wiki/Chomsky_hierarchy
