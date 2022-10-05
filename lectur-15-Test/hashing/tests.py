from selenium import webdriver
from django.test import TestCase
from .forms import HashForm
import hashlib
from .models import Hash

# browser = webdriver.Chrome()
# browser.get("http://127.0.0.1:8000/")


# class FunctionalTestCase(TestCase):
    

#     def setUp(self):
#         self.browser = webdriver.Chrome()



#     def test_there_is_homepage(self):
#         self.browser.get('http://localhost:8000')
#         self.assertIn('Enter hash here',self.browser.page_source)

#     def test_hash_of_hello(self):
#         self.browser.get('http://localhost:8000')
#         # Find the element with id "text"
#         text = self.browser.find_element_by_id("id_text")
#         text.send_keys("hello")
#         self.browser.find_element_by_name("submit").click()
#         self.assertInHTML('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', self.browser.page_source)

#     def tearDown(self):
#         self.browser.quit()


class UnitTestCase(TestCase):


    def test_home_homepage_tempalte(self):
        # Go to the homepage
        response = self.client.get('/')
        # Search for home.html
        self.assertTemplateUsed(response, 'hashing/home.html')

    def test_hash_form(self):
        form = HashForm(data={'text': 'hello'})
        # Check if it is valid
        self.assertTrue(form.is_valid())

    
    def test_hash_func_works(self):
        text_hash = hashlib.sha256('hello'.encode('utf-8')).hexdigest()
        self.assertEqual('2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824', text_hash)

    
    def test_hash_object(self):
        # First create a hash object:
        hash = Hash()
        # the first property will be a sample text, and second will be the corresponding hash value of that text
        hash.text = 'hello'
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        # save new test properties to the db
        hash.save()
        # Get the object from db, django will search for this hash from the db, and bring us the object
        pulled_hash = Hash.objects.get(hash='2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        # Check if the db value is equal to the true one
        self.assertEqual(hash.text,pulled_hash.text)



    def test_viewing_hash(self):
        # Inherit from Hash form:
        hash = Hash()
        # sample text will be 'hello' as always:
        hash.text = 'hello'
        # sample hash is the same as always
        hash.hash = '2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824'
        # save to the test db
        hash.save()
        # the url pattern should be as fallows, hash/<hash value>
        response = self.client.get('/hash/2cf24dba5fb0a30e26e83b2ac5b9e29e1b161e5c1fa7425e73043362938b9824')
        self.assertContains(response,'hello')