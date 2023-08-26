userinit_schema = {
    "$schema" : "http://json-schema.org/draft-04/schema#",
    "title" : "User Input",
    "description" : "A user request json",
    "type" : "object",
    "properties" : {
        "userid" : {
            "description" : "User ID",
            "type" : "string"
        },
        "mtype" : {
            "type" : "string",
            "pattern" : "initialization"
        }
    }
}