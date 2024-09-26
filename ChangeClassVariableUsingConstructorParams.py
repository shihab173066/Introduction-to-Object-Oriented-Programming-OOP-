"""
### Change Class Variable Using Constructor Params
- **Short Explanation:** Class variables can be modified using constructor parameters, impacting all instances.
- **Practice Problem:** Create a class with a class variable for a company name, and change it using constructor parameters.
- **Test Case Output:** 
  - `Company: Google`

"""
class Company:
    company_name = "ABC Inc."

    def __init__(self, company_name=None):
        if company_name:
            Company.company_name = company_name

    @classmethod
    def display_company_name(cls):
        print(f"Company: {cls.company_name}")

company = Company("Google")
Company.display_company_name()