var user = {
    user: "edituser",
    pwd: "Password01",
    roles: [
        {
            role: "dbOwner",
            db: "Sampledb"
        }
    ]
};
db.createUser(user);
db.createCollection('sample');