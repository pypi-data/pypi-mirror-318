# Zinny Surveys: Structured Media Evaluation
[![License](https://img.shields.io/badge/License-BSD%203--Clause-blue.svg)](LICENSE)

##  What's the skinny on the ciné?

Zinny is a tool for rating media, and the surveys here provide for a meaningful evaluation of consistent criteria across many titles and perspectives.

## A collection of survey definitions

This repo is a collection of surveys used by the [zinny-api](https://github.com/RyLaney/zinny-api) and front end [zinny-webui](https://github.com/RyLaney/zinny-webui).  They are published separately to allow for independent use, and to encourage community contributions.

## Installation

see [SETUP.md](https://github.com/RyLaney/zinny-surveys/blob/main/SETUP.md)

## Motivation:
Comparing movies across genres, styles, or time periods can be challenging. Surveys offer a structured approach to evaluate films by breaking down complex elements into measurable components. This approach captures the expertise behind a movie more comprehensively than a single score.

Surveys define measurable criteria, while weights establish their relative importance, making evaluations both meaningful and customizable.

## Goals

* **Standardization:** Standardization: Provide curated surveys and weights for consistent and reliable evaluations.

* **Customization:** Easily create or modify JSON-based surveys and weights to fit specific needs.

* **Community Contributions:** Contributions are welcome to expand criteria or add new surveys. Submit pull requests or reach out to get involved.


## Definitions

### Surveys
## Definitions

### Surveys
**Survey:** A predefined set of criteria for evaluating a media title. Each survey includes:
* **Metadata:** Describes the survey's purpose, version, author, and related details.
* **Criteria:** Individual measures with attributes such as range and descriptions.

**Criteria:**
* Criteria are measurable attributes within a survey, defined as:
  * **ID:** A unique identifier (e.g., "artistry").
  * **Name:** A human-readable label (e.g., "Artistry").
  * **Description:** Details what the criterion measures.
  * **Range:** (optional) Specifies valid scoring values (e.g., [1,10]).
  * **Value Labels:** (optional) Explains specific values within the range (e.g., 0: "No quality", 10: "best quality").

#### Repository Structure
#### Repository Structure

```plaintext
surveys/
├── shared/                     # Institutionally approved surveys
│   ├── vfx.json
│   ├── picture.json
│   └── ...
├── community/                    # Community-contributed surveys
└── local/                        # reserved for local surveys
```

#### Example JSON Representation:
see [Examples.md](https://github.com/RyLaney/zinny-surveys/blob/main/docs/Examples.md)

### Weight Presets
**Weights:**
Weights determine the relative importance of each survey criterion. They are linked to specific surveys (and optionally, survey versions) and allow for multiple perspectives by using different weight configurations.

#### Repository Structure

```plaintext
weights/                          # Weighting configurations
├── shared/                     # Institutionally approved weights
│   ├── vfx_even_weights.json
│   ├── picture_even_weights.json
│   ├── picture_storyteller.json
│   └── picture_technologist.json
├── community/                    # Community-contributed weights
└── local/                        # reserved for local weights
```

## Collections

**Collection:**
Collections group related items, such as titles or surveys, into curated sets. Each collection includes:
  * **ID:** A unique identifier (e.g., "favorites_2024").
  * **Name:** A human-readable name (e.g., "My Favorites").
  * **Description:** Optional context for the collection (e.g., "Movies to watch this year.").
  * **Items:** A list of either titles or surveys in the collection.
    * **Titles:** Include name (e.g., "Madame Web") and year (e.g., 2024).
    * **Surveys:** Include name (e.g., "VFX Evaluation") and version (e.g., "1.0").

## Contributing
We welcome contributions! If you'd like to report an issue, suggest a feature, or contribute code, please check out the [CONTRIBUTING.md](https://github.com/RyLaney/zinny-surveys/blob/main/CONTRIBUTING.md) file for guidelines.

## Acknowledgements
- Development was sponsored by [Teus Media](https://teus.media).
