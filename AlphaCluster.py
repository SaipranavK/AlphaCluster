#Libraries

from datetime import datetime
from flask import Flask,render_template,request
from flask_sqlalchemy import SQLAlchemy


#Config

app=Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///alphacluster.db'
db=SQLAlchemy(app)

#Models

class Locations(db.Model):

    Lid=db.Column(db.Integer,primary_key=True)
    Launch_site_name=db.Column(db.String(100),nullable=False)
    Launch_site_long=db.Column(db.String(100),nullable=False)
    Launch_site_lat=db.Column(db.String(100),nullable=False)
    Space_site_name=db.Column(db.String(100),nullable=False)
    Space_site_long=db.Column(db.String(100),nullable=False)
    Space_site_lat=db.Column(db.String(100),nullable=False)


    def __repr__(self):
        return "# Launch Site: %s\nCordinates: %s, %s  SpacePorts: %s\nCordinates: %s, %s\n"%(self.Launch_site_name,self.Launch_site_long,self.Launch_site_lat,self.Space_site_name,self.Space_site_long,self.Space_site_lat)

class Groups(db.Model):

    Gid=db.Column(db.Integer,primary_key=True)
    Country=db.Column(db.String(100),nullable=False)
    Organisation_name=db.Column(db.String(100),nullable=False)
    
    
    def __repr__(self):
        return "Country: %s \t Organisation: %s "%(self.Country,self.Organisation_name)

    

class Launches(db.Model):
    
    Laid=db.Column(db.Integer,primary_key=True)
    Month=db.Column(db.Integer,nullable=False)
    Year=db.Column(db.Integer,nullable=False)
    Organisation_name=db.Column(db.String(100),nullable=False)
    Booster_version=db.Column(db.String(100),nullable=False)
    Launch_site=db.Column(db.String(100),nullable=False)
    Payload=db.Column(db.String(100),nullable=False)
    Orbit=db.Column(db.String(100),nullable=False)
    Mission=db.Column(db.String(100),nullable=False)

    def __repr__(self):
        return "Month: %s || \t Year: %s || \t Organisation: %s || \t Booster: %s || \t Launch Site: %s || \t Payload: %s || \t Orbit: %s || \t Mission: %s"%(self.Month,self.Year,self.Organisation_name,self.Booster_version,self.Launch_site,self.Payload,self.Orbit,self.Mission)


# Interface & Interactivity


@app.route('/')
def index():
    return render_template('index.html')

@app.route('/locations')
def locations():
    data=Locations.query.all()    
    return render_template('locations.html',data=data)

@app.route('/groups')
def groups():
    data=Groups.query.all()    
    return render_template('groups.html',data=data)

@app.route('/launches')
def launches():
    data=Launches.query.all()    
    return render_template('launches.html',data=data)


