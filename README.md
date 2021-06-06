# Fast_API_Examples

Example of request:
curl -X 'POST' \
  'http://HOST_ADDRESS/multiple' \
  -H 'accept: application/json' \
  -H 'Content-Type: multipart/form-data' \
  -F 'files=@b73827c0-dae8-11ea-a95f-47e6bb2ba811.jpg;type=image/jpeg' \
  -F 'files=@1557584202182978680.jpg;type=image/jpeg' \
  -F 'files=@Drop-in_Extrusion_Nut.4.STL'
  
  Files are saved on the server with the same names and extensions as they were send using the form. In this example - 2 .JPEG files and one .STL
