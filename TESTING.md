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
    
  ![Manual Test Part 1](/static/readme-docs/mt1.png)

  ![Manual Test Part 2](/static/readme-docs/mt2.png)

  ![Manual Test Part 3](/static/readme-docs/mt3.png)

  ![Manual Test Part 4](/static/readme-docs/mt4.png)

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


- The shopping bag was throwing an error about duplicate IDs, this came down to the 2 versions of the shopping bag, one for large screens one for mobile, which used the same include template from quantity-form.html, effectively putting 2 versions of the same code on the page. I solved this by changing the ID attribute to a data-id attribute, and adjusting the relevant JavaScript code.

</details>


  * [Back to Contents](#contents)

  ### CSS
 I ran the CSS code through the [W3C CSS Validator](https://jigsaw.w3.org/css-validator/#validate_by_input). All code passed the validation tests. Results below.


<details><summary>CSS Validation Results Table</summary>

| **Feature**    | **Expected Outcome**                  | **Test Performed**                                   | **Result**                                                                                                              | **Pass / Fail** |
|----------------|---------------------------------------|------------------------------------------------------|-------------------------------------------------------------------------------------------------------------------------|-----------------|
| CSS Validation | Pages passe validation with no errors | Ran CSS through https://jigsaw.w3.org/css-validator/ |  | PASS            |

</details>

   * [Back to Contents](#contents)

   ### JSHINT
  All JS pages were checked with [JSHINT](https://jshint.com/)

  <details>
    <summary>Click to View JSHINT Test Evidence</summary>
  
  ![Stripe_elements](/static/readme-docs/stripe_elements.png)

  ![Quantity-input](/static/readme-docs/quantity-input.png)

  ![CountryField](/static/readme-docs/countryfield.png)

  </details>

  * [Back to Contents](#contents)

  ### PYLINT
  All Python pages were checked with [CODE INSTITUTES PYTHON LINTER](https://pep8ci.herokuapp.com/)

  <details>
    <summary>Click to View Pylint Test Evidence</summary>
    
  ![Views.py from Bag App](/static/readme-docs/bagapp.png)

  ![Views.py from Checkout App](/static/readme-docs/checkout-views.png)

  ![Models.py from Checkout App](/static/readme-docs/checkout-models.png)

  ![Forms.py from Checkout App](/static/readme-docs/checkout-form.png)

  ![Views.py from Home App](/static/readme-docs/home-views.png)

  ![Models.py from Home App](/static/readme-docs/home-models.png)

  ![Models.py from Products App](/static/readme-docs/products-models.png)

  ![Forms.py from Products App](/static/readme-docs/products-form.png)

  ![Views.py from Products App](/static/readme-docs/products-views.png)

  ![Views.py from Profile App](/static/readme-docs/profiles-views.png)

  ![Models.py from Products App](/static/readme-docs/profiles-models.png)

  ![Forms.py from Products App](/static/readme-docs/profiles-form.png)

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
  - The site was tested using [Browserstack](https://www.browserstack.com/) to ensure compatibility across various browsers, Chrome, Safari and Firefox.

  <details>
    <summary>Click to View Browser Test Evidence</summary>
    
  ![Firefox](/static/readme-docs/explorer.png)

  ![Chrome](/static/readme-docs/chrome.png)

  ![Safari](/static/readme-docs/safari.png)

  </details>

  ### Unsolved Bugs
  
  - No unsolved bugs

  * [Back to Contents](#contents)
