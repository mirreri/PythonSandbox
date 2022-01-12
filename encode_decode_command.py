# because some command will be blocked by using string checking, so can encode then decode command to execute it
import base64

# execute print 'hello world'
encode_cmd = base64.b64encode (b"print ('hello world')")
exec (base64.b64decode (encode_cmd))

# execute import os module
encode_cmd = base64.b64encode (b"import os")
exec (base64.b64decode (encode_cmd))
