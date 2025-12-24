from flask import Flask
from flask_mysqldb import MySQL

#DB연결
from sqlalchemy import create_engine, Column, String, Integer
#테이블 생성
from sqlalchemy.orm import declarative_base, sessionmaker

app = Flask(__name__)

#ORM SQLite 연결 - echo : 디버그모드 - 에러메시지 출력
engine = create_engine("sqlite:///users.db", echo=True)

# Base 클래스 정의
Base = declarative_base()

# 테이블 정의
class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, nullable=False)
    
    def __repr__(self):
        return f"<User(id={self.id}, name='{self.name}')>"


#테이블 생성
Base.metadata.create_all(bind=engine)

# 세션 준비
SessionLocal = sessionmaker(bind=engine)


def run_single():
    """
    단일 데이터 핸들링
    """
    db = SessionLocal()

    #CREATE (단일)

    new_user = User(name="OZ_BE16")
    db.add(new_user)
    db.commit()
    print("⭐새로운 사용자 추가: ", new_user)

    #READ (단일)
    user = db.query(User).first()
    print("⭐첫번째 사용자 검색: ", user)


    #UPDATE (단일)
    if user:
        user.name = "OZ_BE16_Updated"
        db.commit()
        print("⭐사용자 업데이트: ", user)

    #DELETE (단일)
    if user:
        db.delete(user)
        db.commit()
        print("⭐사용자 삭제됨")


    db.close()


def run_bulk():
    """
    복수 데이터 핸들링
    """
    db = SessionLocal()

    #CREATE
    users = [User(name="OZ_BE15"), User(name="BE16"), User(name="OZ_BE17")]
    db.add_all(users)
    db.commit()
    print("⭐복수 사용자 추가: ", users)

    #READ

    #전체조회
    # users_all = db.query(User).all() - DB 데이터가 많으면 DB에 부하가 걸림. 잘 안쓴다.
                                        #SELECT * FROM User

    #조건 조회
    be16_users = db.query(User).filter(User.name=="BE16").all()
    print("⭐조건 조회: ", be16_users)

    #패턴 검색
    oz_users = db.query(User).filter(User.name.like("OZ_%")).all()
    print("⭐패턴 검색: ", oz_users)

    #UPDATE
    if oz_users:
        for user in oz_users:
            user.name = user.name + "_NEW"
        db.commit()
    print("⭐복수 사용자 업데이트: ", oz_users)

    #DELETE
    #DB 데이터 전체 삭제
    db.query(User).delete()
    db.commit()
    print("⭐사용자 전체 삭제")

    db.close()




if __name__ == "__main__":
    # run_single()
    run_bulk()
    # app.run(debug=True)



