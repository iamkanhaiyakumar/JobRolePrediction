from fastapi import APIRouter, UploadFile, File, Header
from backend.utils.jwt_handler import decode_access_token

router = APIRouter()

@router.post("/admin/upload")
def upload_csv(file: UploadFile = File(...), token: str = Header(...)):
    user = decode_access_token(token.split(" ")[1])
    if not user or user["role"] != "admin":
        return {"message": "Unauthorized"}

    file_location = f"backend/data/{file.filename}"
    with open(file_location, "wb+") as f:
        f.write(file.file.read())

    return {"message": f"File {file.filename} uploaded successfully"}
