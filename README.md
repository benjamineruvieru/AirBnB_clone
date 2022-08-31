# AirBnB clone
**A clone of the AirBnB software**

![](https://s3.amazonaws.com/alx-intranet.hbtn.io/uploads/medias/2018/6/65f4a1dd9c51265f49d0.png?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIARDDGGGOUSBVO6H7D%2F20220831%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20220831T150043Z&X-Amz-Expires=86400&X-Amz-SignedHeaders=host&X-Amz-Signature=6f9b09f04380c77e7604197fc582fba3994cd21a7cf95b545c2969c311557072)

## First step - `The Console`
### 0x00. AirBnB clone - The console

This step involves building a command interpreter to manage your AirBnB objects.
This first step is very important because it will be used during this project with all other following projects: HTML/CSS templating, database storage, API, front-end integration…

Each task is linked and will help you to:

- put in place a parent class (called BaseModel) to take care of the initialization, serialization and deserialization of your future instances
- create a simple flow of serialization/deserialization: Instance <-> Dictionary <-> JSON string <-> file
- create all classes used for AirBnB (User, State, City, Place…) that inherit from BaseModel
- create the first abstracted storage engine of the project: File storage.
- create all unittests to validate all our classes and storage engine

### What’s a command interpreter?
*we want to be able to manage the objects of our project:*

- Create a new object (ex: a new User or a new Place)
- Retrieve an object from a file, a database etc…
- Do operations on objects (count, compute stats, etc…)
- Update attributes of an object
- Destroy an object