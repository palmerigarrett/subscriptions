This is the technical assessment challenge for the engineering role on the Subscriptions Team, at [The Atlantic](https://www.theatlantic.com). Please follow the instructions carefully.

## Background
The following is a hypothetical situation that would require some engineering and database design. Imagine we have an external e-commerce vendor that handles ordering of our subscription products. We'd like to have a copy of our subscription related records in an internal database that we can query directly. Let's assume we have a web-hook setup to listen for changes that occur in our external vendor.

## Deliverable
* Using Python (Django a plus) create a web application with an API endpoint that accepts information from our vendor, parses it, then inserts or updates record(s) in a relational database accordingly.
* Include the database schema.
* Your web application does not need authentication or authorization capabilities.

Below is an example post request the endpoint should consume.
* price in cents

```json
  {
    "customer": {
      "id": "b73b8b0e-0240-42a9-874c-00445d51dd8a",
      "first_name": "Ernest",
      "last_name": "Hemingway",
      "address_1": "907 Whitehead St",
      "address_2": "",
      "city": "Key West",
      "state": "FL",
      "postal_code": "33043",
      "subscription": {
        "id": "eac8709f-d898-42f0-84d8-a1997c25cae9",
        "plan_name": "print & digital",
        "price": "5999",
      },    
      "gifts":[
        {
          "id": "53368db4-6097-49c6-ba8b-b00ab4a3ce3b",
          "plan_name": "digital",
          "price": "4999",
          "recipient_email": "mark@twain.com"
        },
        {
          "id": "fb7a077b-928f-4d44-a2e5-6969c72d3b45",
          "plan_name": "digital",
          "price": "4999",
          "recipient_email": "jane@austin.com"
        }
      ]
    }
  }
```
Please include instructions describing the process to setup/install any prerequisite software, initialize the relational database, and run the web application.

## Submission
Please email [sjaromirski@theatlantic.com](mailto:sjaromirski@theatlantic.com) with one of the following:
1. The URL of a public GitHub (or GitLab) repository that contains your code and instructions.
1. A gzipped tarball containing a git repository with your code and instructions.

## Evaluation Criteria
Your submission will be evaluated primarily on your adherence to the instructions and on the functional completeness of the solution.

Extra points will be awarded for:
* Tests.
* Irregularity detection and alerting (for instance, if record with a new id is posted with the same email as an existing record.).
* Read endpoint(s).
* A full git history showing your development style.
* Dockerization of application.

## Notes
* The goal is to see what you are able to accomplish in maximum 2 hours. If you're still working after 2 hours, please just document (1) what you were able to complete and (2) what you would do if you were to devote more time to the challenge - and then submit those descriptions along with whatever code you've completed (following the Submission instructions above).
* Please submit your solution within a few days of receiving the challenge.
* Please feel free to email [sjaromirski@theatlantic.com](mailto:sjaromirski@theatlantic.com) with any questions.