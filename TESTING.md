# PROJECT TEST DOC - Fetch

## CONTENTS
* [TESTS PERFORMED](#tests-performed)
  * [Manual User Story Tests](#manual-user-story-tests)
  * [HTML](#html)
  * [CSS](#css)
  * [Lighthouse](#lighthouse)
  * [JSHINT](#jshint)
  * [PYLINT](#pylint)
  * [Browser Compatability](#browser-compatability)
  * [Unsolved Bugs](#unsolved-bugs)

  [Return to README.md](https://github.com/)


## TESTS PERFORMED
  The site was thoroughly tested during development. The tests included:
  1. Early user observation test
  2. Manual user story tests
  3. HTML, CSS, JSHINT, PYLINT, Lighthouse, PEP8
  4. Browser Compatability Tests

  ### Manual User Story Tests
  User story tests were conducted systematically, with any failing tests rectified. 
  <details>
    <summary>Click to View Manual User Story Test Evidence</summary>
    <br>
      - <img src="static/docs/" width="60%">
      <br>
      - <img src="static/docs/" width="60%">
      <br>
      - <img src="static/docs/" width="60%">
      <br>
      - <img src="static/docs/" width="60%">
      <br>
      - <img src="" width="60%">
      <br>
    

  </details>

  * [Back to Contents](#contents)

  ### HTML
  I ran the code for all the pages through the [W3C HTML Validator](https://validator.w3.org/nu/) using the textarea input by generating the source code from the deployed site (right click and select 'View Page Source' in Chrome) and pasting it in to allow me to check all pages whether requiring log in or not. All code passed the validation tests. Results below.


<details><summary>HTML Validation Results Table</summary>

| **Feature** | **Expected Outcome** | **Test Performed** | **Result** | **Pass / Fail** |
|---|---|---|---|---|
| **HOME** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **PRODUCTS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **PRODUCT DETAILS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **ADD PRODUCT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Form table errors & custom clearable fit input issue - resolved | PASS |
| **EDIT PRODUCT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Form table errors & custom clearable fit input issue - resolved | PASS |
| **ADD REVIEW** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **EDIT REVIEW** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **BAG** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | Duplicate ID error - resolved | PASS |
| **CHECKOUT** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **CHECKOUT SUCCESS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **PROFILE** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **FAQS** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |
| **CONTACT US** | Page passes validation with no errors | Ran page through https://validator.w3.org/nu/ | No errors | PASS |


</details>


  * [Back to Contents](#contents)

  ### CSS
 I ran the CSS code through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). All code passed the validation tests. Results below.


<details><summary>CSS Validation Results Table</summary>

| **Feature**    | **Expected Outcome**                  | **Test Performed**                                   | **Result**                                                                                                              | **Pass / Fail** |
|----------------|---------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| CSS Validation | Page passes validation with no errors | Ran CSS through https://jigsaw.w3.org/css-validator/ |  | PASS            |

</details>

   * [Back to Contents](#contents)

   ### JSHINT
  All JS pages were checked with [JSHINT](https://jshint.com/)

  <details>
    <summary>Click to View JSHINT Test Evidence</summary>
      - <img src="" width="60%">

  </details>

  * [Back to Contents](#contents)

  ### PYLINT
  All Python pages were checked with [CODE INSTITUTES PYTHON LINTER](https://pep8ci.herokuapp.com/)

  <details>
    <summary>Click to View PYLINT Test Evidence</summary>
      - Views.py from User App
      <br>
      - <img src="https://res.cl" width="60%">
      <br>
      - Views.py from Offer App
      <br>
      - <img src="https://" width="60%">
      <br>
      - Models.py from Offer App
      <br>
      - <img src="https://" width="60%">
      <br>
      - Forms.py from Offer App
      <br>
      - <img src="https://re" width="60%">
      <br>
      - Forms.py from User App
      <br>
      - <img src="https:/" width="60%">
      <br>
      - Urls.py from Offer App
      <br>
      - <img src="https://r" width="60%">
      <br>

  </details>

  * [Back to Contents](#contents)

  ### LIGHTHOUSE
  A lighthouse report was run on the site following deployment on the Home Page
  * The performance issues are related to image sizes and have been noted in the Future Enhancements

  <details>
    <summary>Click to View LightHouse Test Evidence</summary>
      - <img src="https://" width="60%">
      <br>
      - <img src="https://" width="60%">
      <br>

  </details>

  * [Back to Contents](#contents)

  ### PEP8
  During development, any PEP8 problems in the IDE tab were addressed.  The following were left as they are in the settings and env.py files and relate to specific links or security keys.

  <details>
    <summary>Click to View PEP8 Evidence</summary>
      - <img src="https://" width="60%">

  </details>

  * [Back to Contents](#contents)

  ### Browser Compatability
  - The site was tested using [Browserstack](https://www.browserstack.com/) to ensure compatibility across various browsers, Windows and Android, Chrome, Safari and Firefox.

  <details>
    <summary>Click to View Browser Test Evidence</summary>
      - <img src="/static/readme-docs/explorer.png" width="60%">
      <br>
      - <img src="/static/readme-docs/chrome.png" width="60%">
      <br>
      - <img src="/static/readme-docs/safari.png" width="60%">
      <br>
      

  </details>

  ### Unsolved Bugs
  
  - No unsolved bugs

  * [Back to Contents](#contents)
