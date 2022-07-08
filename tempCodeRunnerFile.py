 if('NAME' in i or 'Name' in i or 'name' in i or 'username' in i or 'USERNAME' in i or 'Username' in i or 'user' in i or 'User' in i or 'USER' in i):
        print('NAME1')
        with open('html.txt','a') as f:
            # content = f.read()
            text="""<label  class="input">NAME</label>
    <br>
    <br>
    <input type="text" name="NAME" class="inputbox" placeholder="NAME">
    <br>
    <br>"""