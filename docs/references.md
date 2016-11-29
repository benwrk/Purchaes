
function | description | parameter | return
---------|-------------|-----------|-------
login | login to the member area | username,password | token/fail
logout | logout from user area | token | success/fail
auth | authenticate user when access the member area | token | success/fail
register | registering | username,password,email | success/fail
get_items | getting the list of item that macth the keyword | name | name,discription,image url,item_ id
suggestion | get the suggesstion when searchig for a word | name | name
post | post a new order | name, discription, image, tag | success/fail
delete | delete order for the account | id | success/fail
