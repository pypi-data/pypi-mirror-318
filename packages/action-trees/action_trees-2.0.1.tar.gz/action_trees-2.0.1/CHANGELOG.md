# Changelog
All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/), and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## Unreleased

## v2.0.1

* remove exception trace
* add `._on_init` stub



## v2.0.0

* REMOVE `.id` (was snowflake)
* add `.__str__`

## v1.0.0

* ADD `get_child_by_name`
* REMOVE `get_child` function
* refactor (remove protocols etc)
* update examples
* add `tasks.py` for devops management.

## v0.3.7

* add `ActionItem.id`  = auto-generated snowflake id
* make `name` optionall, defaulting to `__class__.__name__`


## v0.3.5

* improve typehinting


## v0.3.4

* consolidate config to `pyproject.toml`


## v0.3.2

* remove `click` dependency
* change method to private: `_start_children_parallel()`

## v0.3.1

* set package status to *beta*


## v0.3.0

* add `start_children_parallel()` method
* fix typehinting
* include "coffee maker" example
* update README


## v0.2.0

* add state transition checks


## v0.1.0

* move code from `roxbot` to this repo.
