from flask import Flask, request
import models, utility
from database import Session, Base, create_engine, eng
import traceback, os


app = Flask(__name__)

@app.route("/user/signup/", methods= ["POST"])
def signup(db = Session()):
    try:
        payload = dict(request.get_json())
        email = payload["email"]
        check_db = db.query(models.Employee).filter(models.Employee.employee_email == email).first()
        if check_db!=None:
            db.close()
            return {"detail":f"{email} already exists"}
        password = utility.get_password_hashed(payload["password"])

        new_employee = models.Employee()
        new_employee.employee_name = payload["name"]
        new_employee.employee_email = email
        new_employee.password = password

        db.add(new_employee)
        
        db.commit()
        db.refresh(new_employee)
        db.close()

        return {"detail":"new employee created", "employee_id":new_employee.employee_id}, 201

    except Exception as err:
        db.close()
        traceback.print_exc()
        return {"detail":str(err)}, 401



if __name__ == "__main__":
    if not os.path.exists("test.db"):
        Base.metadata.create_all(eng)
    app.run(debug=True)