define({ "api": [
  {
    "version": "0.0.1",
    "type": "post",
    "url": "/hackathons/:id",
    "title": "1. Create Hackathon Member",
    "name": "CreateHackathonMember",
    "group": "HackathonMembers",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Hackathon ID.</p>"
          },
          {
            "group": "Parameter",
            "type": "String",
            "optional": false,
            "field": "role",
            "description": "<p>O(Organiser)/ M (Mentor)/ P (Participant)/ V (Volunteer)</p>"
          }
        ]
      },
      "examples": [
        {
          "title": "Request Data Example:",
          "content": "{\n    \"id\": \"github_12345\",\n    \"role\": \"M\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "HackathonMembers"
  },
  {
    "version": "0.0.1",
    "type": "delete",
    "url": "/hackathon/:id",
    "title": "5. Delete Hackathon",
    "name": "DeleteHackathonMember",
    "group": "HackathonMembers",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Hackathon ID.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user-id",
            "description": "<p>User ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 204 NO CONTENT",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "HackathonMembers"
  },
  {
    "version": "0.0.1",
    "type": "get",
    "url": "/hackathons/:id",
    "title": "2. Get Hackathon Members",
    "name": "GetAllMembersForHackathon",
    "group": "HackathonMembers",
    "success": {
      "examples": [
        {
          "title": "Sample Success Response",
          "content": "\n[\n    {\n        \"hackathon\": 1,\n        \"member\": \"github_12345\",\n        \"role\": \"P\"\n    },\n    .\n    .\n    {\n        \"hackathon\": 1,\n        \"member\": \"facebook_4342\",\n        \"role\": \"M\"\n    }\n]\n\nSuccess Response Code: HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "HackathonMembers"
  },
  {
    "version": "0.0.1",
    "type": "get",
    "url": "/hackathon/:id/members/:user-id",
    "title": "3. Get Hackathon Member",
    "name": "GetHackathonMember",
    "group": "HackathonMembers",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Hackathon ID.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user-id",
            "description": "<p>User ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "HackathonMembers"
  },
  {
    "version": "0.0.1",
    "type": "put",
    "url": "/hackathon/:id/members/:user-id",
    "title": "4. Update Hackathon",
    "name": "UpdateHackathonMember",
    "group": "HackathonMembers",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Hackathon ID.</p>"
          },
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "user-id",
            "description": "<p>User ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "HackathonMembers"
  },
  {
    "version": "0.0.1",
    "type": "post",
    "url": "/hackathons/",
    "title": "1. Create Hackathon",
    "name": "CreateHackathon",
    "group": "Hackathons",
    "description": "<p>NOTE: Schema to send is in 'Request Data Sample'</p>",
    "parameter": {
      "examples": [
        {
          "title": "Request Data Example:",
          "content": "{\n    \"id\": 1,\n    \"data\": {\n        \"exampleHackathonData\": {\n            \"Name\": \"Penapps\"\n        }\n    }\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 201 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "Hackathons"
  },
  {
    "version": "0.0.1",
    "type": "delete",
    "url": "/hackathon/:id",
    "title": "5. Delete Hackathon",
    "name": "DeleteHackathon",
    "group": "Hackathons",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Hackathon unique ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 204 NO CONTENT",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "Hackathons"
  },
  {
    "version": "0.0.1",
    "type": "get",
    "url": "/hackathons/",
    "title": "2. Get All Hackathons",
    "name": "GetAllHackathons",
    "group": "Hackathons",
    "success": {
      "examples": [
        {
          "title": "Sample Success Response:",
          "content": "\n[\n    {\n        \"id\": 1,\n        \"data\": {\n            ...\n        },\n        \"is_published\": false\n    },\n    {\n        \"id\": 5,\n        \"data\": {\n            ...\n        },\n        \"is_published\": false\n    }\n]\n\nSuccess Response Code: HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "Hackathons"
  },
  {
    "version": "0.0.1",
    "type": "get",
    "url": "/hackathon/:id",
    "title": "3. Get Hackathon",
    "name": "GetHackathon",
    "group": "Hackathons",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Hackathon unique ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "Hackathons"
  },
  {
    "version": "0.0.1",
    "type": "put",
    "url": "/hackathon/:id",
    "title": "4. Update Hackathon",
    "name": "UpdateHackathon",
    "group": "Hackathons",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>Hackathon unique ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/hackathon_view.py",
    "groupTitle": "Hackathons"
  },
  {
    "version": "0.0.1",
    "name": "HeadersRequired",
    "type": "headers",
    "url": "/*",
    "title": "To pass for API Authentication and Response",
    "group": "Headers",
    "description": "<p>These headers need to passed along with every API request</p>",
    "header": {
      "examples": [
        {
          "title": "Headers:",
          "content": "{\n    \"Content-Type\": \"application/json\"\n    \"Authorisation\": \"Bearer JWT_TOKEN\"\n}",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/root_view.py",
    "groupTitle": "Headers"
  },
  {
    "version": "0.0.1",
    "type": "post",
    "url": "/users/",
    "title": "1. Create User",
    "name": "CreateUser",
    "group": "Users",
    "parameter": {
      "examples": [
        {
          "title": "Request Data Example:",
          "content": "{\n    \"id\": \"github_12345\"\n}",
          "type": "json"
        }
      ]
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 201 Created",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user_view.py",
    "groupTitle": "Users"
  },
  {
    "version": "0.0.1",
    "type": "delete",
    "url": "/User/:id",
    "title": "4. Delete User",
    "name": "DeleteUser",
    "group": "Users",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>User ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 204 NO CONTENT",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user_view.py",
    "groupTitle": "Users"
  },
  {
    "version": "0.0.1",
    "type": "get",
    "url": "/users/:id",
    "title": "2. Get User",
    "name": "GetUser",
    "group": "Users",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>User ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user_view.py",
    "groupTitle": "Users"
  },
  {
    "version": "0.0.1",
    "type": "put",
    "url": "/users/:id",
    "title": "3. Update User",
    "name": "UpdateUser",
    "group": "Users",
    "parameter": {
      "fields": {
        "Parameter": [
          {
            "group": "Parameter",
            "type": "Number",
            "optional": false,
            "field": "id",
            "description": "<p>User ID.</p>"
          }
        ]
      }
    },
    "success": {
      "examples": [
        {
          "title": "Success Response Code:",
          "content": "HTTP/1.1 200 OK",
          "type": "json"
        }
      ]
    },
    "filename": "api/views/user_view.py",
    "groupTitle": "Users"
  }
] });
