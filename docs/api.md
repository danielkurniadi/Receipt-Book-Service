# `Receipt API`

Everything related to the receipt image file, including:
- receipt image to text analysis (OCR)
- receipt image file storage (upload, download, delete)


## Notes

```python
# Error Codes
ServerOk = 0
ServerError = 1
DatabaseError = 2
OperationNotSupported = 3
```


## `POST api/receipts/summary` (Multipart/Form-data)
Summarize receipt image (file) using OCR

#### Request
```form-data
"file": [choose file]
```

#### Response (Success)

```json
{
  "result": true,
  "error_code": 0,
  "data": {
    "date": "12-09-2018",
    "market": "Grocery",
    "totalSum": 0.99
  }
}
```

## `POST api/receipts/create` (Multipart/Form-data)

Upload receipts. Then create it's metadata in db.

#### Request

```form-data
{
  "file": [choose file]
}
```

#### Response

```json
{
  "result": true,
  "error_code": 0,
  "receipt": {
    "id": "7987132418921423",
    "filename": "MacSpicyReceipt-12-09-2018.jpg"
  }
}
```

## `GET api/receipt/<receipt_id>`

Get/download receipt image file

#### Response (application/octet-stream)
Return an image stream directly to the client
```application/octet-stream
[receiptfileimage.jpg]
```

## `PUT api/receipts/update`

Update receipt metadata. For now only update filename is available

#### Request

```json
{
  "id": "7987132418921423",
  "filename": "MacNotSoSpicyReceipt-12-09-2018.jpg"
}
```

#### Response

```json
{
  "result": true,
  "error_code": 0,
  "data": {
    "id": "7987132418921423",
    "filename": "MacNotSoSpicyReceipt-12-09-2018.jpg"
  }
}
```

## `DELETE api/receipt/<receipt_id>/delete`

Delete receipt file/image from filestorage

Response

```json
{
  "result": true,
  "error_code": 0
}
```
