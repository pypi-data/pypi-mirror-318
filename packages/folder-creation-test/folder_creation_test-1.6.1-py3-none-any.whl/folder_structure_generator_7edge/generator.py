import os
import yaml
from InquirerPy import inquirer
import shutil
import importlib.resources  # For locating resources in the installed package


def to_camel_case(name):
    parts = name.split('-')
    # Capitalize the first letter of each part except the first
    return parts[0] + ''.join(word.capitalize() for word in parts[1:])


def create_cognito_user_pool_configuration(pool_name, client_name):
    """
    Creates comprehensive Cognito User Pool configuration with roles and SSM parameters
    Stage is handled by serverless deployment

    :param pool_name: Name of the Cognito User Pool
    :param client_name: Name of the Cognito User Pool Client
    :return: Dictionary containing Cognito resources configuration
    """

    cloudformation_pool_name = to_camel_case(pool_name) 
    return {
        f"{cloudformation_pool_name}UserPool": {
            "Type": "AWS::Cognito::UserPool",
            "Properties": {
                "UserPoolName": f"{pool_name}"+"-${self:provider.stage}",
                "Policies": {
                    "PasswordPolicy": {
                        "MinimumLength": 8,
                        "RequireUppercase": True,
                        "RequireLowercase": True,
                        "RequireNumbers": True,
                        "RequireSymbols": True,
                        "TemporaryPasswordValidityDays": 7
                    }
                },
                "DeletionProtection": "INACTIVE",
                "Schema": [
                    {
                        "Name": "sub",
                        "AttributeDataType": "String",
                        "DeveloperOnlyAttribute": False,
                        "Mutable": False,
                        "Required": True,
                        "StringAttributeConstraints": {
                            "MinLength": "1",
                            "MaxLength": "2048"
                        }
                    },
                    {
                        "Name": "name",
                        "AttributeDataType": "String",
                        "DeveloperOnlyAttribute": False,
                        "Mutable": True,
                        "Required": False,
                        "StringAttributeConstraints": {
                            "MinLength": "0",
                            "MaxLength": "2048"
                        }
                    },
                    {
                        "Name": "email",
                        "AttributeDataType": "String",
                        "DeveloperOnlyAttribute": False,
                        "Mutable": True,
                        "Required": True,
                        "StringAttributeConstraints": {
                            "MinLength": "0",
                            "MaxLength": "2048"
                        }
                    },
                    {
                        "Name": "status",
                        "AttributeDataType": "String",
                        "DeveloperOnlyAttribute": False,
                        "Mutable": True,
                        "Required": False,
                        "StringAttributeConstraints": {
                            "MinLength": "0",
                            "MaxLength": "2048"
                        }
                    },
                    {
                        "Name": "role",
                        "AttributeDataType": "String",
                        "DeveloperOnlyAttribute": False,
                        "Mutable": True,
                        "Required": False,
                        "StringAttributeConstraints": {
                            "MaxLength": "2048"
                        }
                    },
                    {
                        "Name": "created_at",
                        "AttributeDataType": "String",
                        "DeveloperOnlyAttribute": False,
                        "Mutable": True,
                        "Required": False
                    },
                    {
                        "Name": "latest_updated_at",
                        "AttributeDataType": "String",
                        "DeveloperOnlyAttribute": False,
                        "Mutable": True,
                        "Required": False
                    }
                ],
                "UsernameAttributes": ["email"],
                "AutoVerifiedAttributes": ["email"],
                "MfaConfiguration": "OPTIONAL",
                "EnabledMfas": ["SOFTWARE_TOKEN_MFA"],
                "EmailConfiguration": {
                    "EmailSendingAccount": "COGNITO_DEFAULT"
                },
                "UsernameConfiguration": {
                    "CaseSensitive": False
                },
                "AccountRecoverySetting": {
                    "RecoveryMechanisms": [
                        {
                            "Priority": 1,
                            "Name": "verified_email"
                        }
                    ]
                }
            }
        },
        f"{cloudformation_pool_name}UserPoolClient": {
            "Type": "AWS::Cognito::UserPoolClient",
            "Properties": {
                "AccessTokenValidity": 60,
                "AllowedOAuthFlowsUserPoolClient": False,
                "AuthSessionValidity": 5,
                "ClientName": f"{client_name}"+"-${self:provider.stage}",
                "UserPoolId": {"Ref": f"{cloudformation_pool_name}UserPool"},
                "EnablePropagateAdditionalUserContextData": False,
                "EnableTokenRevocation": True,
                "ExplicitAuthFlows": [
                    "ALLOW_CUSTOM_AUTH",
                    "ALLOW_REFRESH_TOKEN_AUTH",
                    "ALLOW_USER_SRP_AUTH",
                    "ALLOW_USER_PASSWORD_AUTH",
                    "ALLOW_ADMIN_USER_PASSWORD_AUTH"
                ],
                "IdTokenValidity": 5,
                "PreventUserExistenceErrors": "ENABLED",
                "RefreshTokenValidity": 30,
                "TokenValidityUnits": {
                    "AccessToken": "minutes",
                    "IdToken": "minutes",
                    "RefreshToken": "days"
                }
            }
        },
        f"{cloudformation_pool_name}IdentityPool": {
            "Type": "AWS::Cognito::IdentityPool",
            "Properties": {
                "IdentityPoolName": f"{pool_name}"+"-${self:provider.stage}",
                "AllowUnauthenticatedIdentities": True,
                "AllowClassicFlow": True,
                "CognitoIdentityProviders": [{
                    "ClientId": {"Ref": f"{cloudformation_pool_name}UserPoolClient"},
                    "ProviderName": {"Fn::GetAtt": [f"{cloudformation_pool_name}UserPool", "ProviderName"]},
                    "ServerSideTokenCheck": False
                }]
            }
        },
        f"{cloudformation_pool_name}IdentityPoolRoleAttachment": {
            "Type": "AWS::Cognito::IdentityPoolRoleAttachment",
            "Properties": {
                "IdentityPoolId": {"Ref": f"{cloudformation_pool_name}IdentityPool"},
                "Roles": {
                    "authenticated": {"Fn::GetAtt": [f"{cloudformation_pool_name}AuthRole", "Arn"]}
                }
            }
        },
        f"{cloudformation_pool_name}AuthRole": {
            "Type": "AWS::IAM::Role",
            "Properties": {
                "AssumeRolePolicyDocument": {
                    "Version": "2012-10-17",
                    "Statement": [{
                        "Effect": "Allow",
                        "Principal": {
                            "Federated": "cognito-identity.amazonaws.com"
                        },
                        "Action": "sts:AssumeRoleWithWebIdentity",
                        "Condition": {
                            "StringEquals": {
                                "cognito-identity.amazonaws.com:aud": {"Ref": f"{cloudformation_pool_name}IdentityPool"}
                            },
                            "ForAnyValue:StringLike": {
                                "cognito-identity.amazonaws.com:amr": "authenticated"
                            }
                        }
                    }]
                },
                "Policies": [{
                    "PolicyName": "CognitoAuthorizedPolicy",
                    "PolicyDocument": {
                        "Version": "2012-10-17",
                        "Statement": [{
                            "Effect": "Allow",
                            "Action": [
                                "s3:PutObject",
                                "s3:GetObject",
                                "s3:PutObjectAcl"
                            ],
                            "Resource": [
                                "arn:aws:s3:::${ssm:BUCKET_NAME}",
                                "arn:aws:s3:::${ssm:BUCKET_NAME}/*"
                            ]
                        }]
                    }
                }]
            }
        },
        # SSM Parameters
        f"{cloudformation_pool_name}CognitoPoolIDStore": {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Name": "COGNITO_USER_POOL_ID",
                "Type": "String",
                "Value": {"Ref": f"{cloudformation_pool_name}UserPool"}
            }
        },
        f"{cloudformation_pool_name}CognitoClientIDStore": {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Name": "COGNITO_CLIENT_ID",
                "Type": "String",
                "Value": {"Ref": f"{cloudformation_pool_name}UserPoolClient"}
            }
        },
        f"{cloudformation_pool_name}CognitoIdentityPoolIDStore": {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Name": "COGNITO_IDENTITY_POOL_ID",
                "Type": "String",
                "Value": {"Ref": f"{cloudformation_pool_name}IdentityPool"}
            }
        },
        f"{cloudformation_pool_name}CognitoPoolARNStore": {
            "Type": "AWS::SSM::Parameter",
            "Properties": {
                "Name": "COGNITO_AUTH_ARN",
                "Type": "String",
                "Value": {"Fn::GetAtt": [f"{cloudformation_pool_name}UserPool", "Arn"]}
            }
        }
    }


def create_dynamodb_table_configuration(table_name, partition_key, sort_key, lsi_keys=None):
    """
    Dynamically creates the DynamoDB table configuration with the given keys and LSIs.

    :param table_name: Name of the DynamoDB table
    :param partition_key: Partition key for the DynamoDB table
    :param sort_key: Sort key for the DynamoDB table
    :param lsi_keys: List of tuples containing LSI name and sort key
    :return: The DynamoDB table configuration as a dictionary
    """
    # Create the table's primary key schema and attributes
    table_config = {
        table_name: {
            "Type": "AWS::DynamoDB::Table",
            "Properties": {
                "TableName": table_name,
                "AttributeDefinitions": [
                    {"AttributeName": partition_key, "AttributeType": "S"},
                    {"AttributeName": sort_key, "AttributeType": "S"}
                ],
                "KeySchema": [
                    {"AttributeName": partition_key, "KeyType": "HASH"},
                    {"AttributeName": sort_key, "KeyType": "RANGE"}
                ],
                "BillingMode": "PAY_PER_REQUEST",
                "LocalSecondaryIndexes": []
            }
        }
    }

    # Add LSIs if provided
    if lsi_keys:
        lsi_configurations = []
        for lsi_name, lsi_sort_key in lsi_keys:
            table_config[table_name]["Properties"]["AttributeDefinitions"].append(
                {"AttributeName": lsi_sort_key, "AttributeType": "S"}
            )
            lsi_configuration = {
                "IndexName": lsi_name,
                "KeySchema": [
                    {"AttributeName": partition_key, "KeyType": "HASH"},
                    {"AttributeName": lsi_sort_key, "KeyType": "RANGE"}
                ],
                "Projection": {
                    "ProjectionType": "ALL"  # You can customize the projection type if needed
                }
            }
            lsi_configurations.append(lsi_configuration)

        # Add LSIs to the table configuration
        table_config[table_name]["Properties"]["LocalSecondaryIndexes"] = lsi_configurations

    return table_config


def create_folder_structure_with_files():
    """
    Creates a folder structure in the current working directory and copies all files 
    from the source folder into the newly created structure.

    :param source_folder: The path to the folder containing the files to copy.
    """
    try:
        base_package_path = importlib.resources.files(
            'folder_structure_generator_7edge')

        # Replace with the actual path
        source_folder = f"{base_package_path}/backend_folder"

        # Define the root directory (current working directory)
        target_folder = os.getcwd()

        os.makedirs(f"{target_folder}/services", exist_ok=True)
        os.makedirs(f"{target_folder}/runbooks", exist_ok=True)

        # Copy all files from the source folder into the target folder
        if os.path.exists(source_folder):
            shutil.copytree(source_folder, target_folder, dirs_exist_ok=True)
            print("Folders created. Please navigate to the service folder and run the 'create' command to set up a new service.")
        else:
            print(f"Source folder '{source_folder}' does not exist.")

    except Exception as e:
        print(f"An error occurred while creating the folder structure: {e}")


# Function to create necessary directories
def create_directories(folders):
    for folder in folders:
        os.makedirs(folder, exist_ok=True)
        print(f"Created folder: {folder}")

# Function to create handler files with boilerplate content


def create_handler_files(base_dir, handler_files, language_choice, file_extension):
    for file_name in handler_files:
        file_path = os.path.join(base_dir, "handlers", f"{file_name}.{file_extension}")
        content = ""

        if language_choice == "Python":
            content = """import json
import boto3
from marshmallow import Schema, fields, ValidationError
from lib.helper import headers



# Define Marshmallow schema
class InputSchema(Schema):
    field1 = fields.Str(required=True)  # Example field, replace with your actual field
    field2 = fields.Int(required=True)  # Example field, replace with your actual field
    # Add your own fields here

def handler(event, context):
    try:
        # Log the event
        print('Event:', json.dumps(event))

        # Parse and validate request body
        body = json.loads(event.get('body', '{}'))

        try:
            schema = InputSchema()
            validated_data = schema.load(body)
        except ValidationError as err:
            return {
                "statusCode": 400,
                "headers": headers,
                "body": json.dumps(
                    {
                        "success_status": False,
                        "message": next(iter(err.messages.values()))[0],
                    }
                ),
            }

        # Business logic goes here
        print('Validated data:', validated_data)

        return {
            'statusCode': 200,
            "headers": headers,

            'body': json.dumps({ "success_status": True, 'message': 'Success'})
        }

    except Exception as error:
        print('Error:', error)
        return {
            'statusCode': 500,
            "headers": headers,

            'body': json.dumps({"success_status": False, 'message': 'There was an error while creating the template'})
        }
"""
        else:
            content = """const AWS = require('aws-sdk')
const Joi = require('joi');
const helpers = require('./lib/helper');  // Import the entire helper.js file



/**
 * AWS Lambda handler function
 * @param {Object} event - Lambda event object
 * @param {Object} context - Lambda context object
 * @returns {Object} Lambda response
 */

 // Define Joi validation schema
const schema = Joi.object({
    field1: Joi.string().required(), // Example field, replace with your actual field
    field2: Joi.number().required(), // Example field, replace with your actual field
    // Add your own fields here
});


module.exports.handler = async (event, context) => {
    try {
        console.log('Event:', JSON.stringify(event))

        // Parse and validate request body
        const body = JSON.parse(event.body);
        const validationResult = schema.validate(body)
        if (validationResult.error) {
            const errorMessage = (validationResult.error.details[0].type === 'object.unknown') ? 'Please fill in all the mandatory fields' : validationResult.error.message
            return {
                statusCode: 400,
                headers: helpers.headers(),
                body: JSON.stringify({ message: errorMessage }),
            }
        }

        return {
            statusCode: 200,
            headers: helpers.headers(),
            body: JSON.stringify({ success_status: true, message: 'Success' })
        }

    } catch (error) {
        console.error('Error:', error)
        return {
            statusCode: 500,
            headers: helpers.headers(),
            body: JSON.stringify({ success_status: false, message: 'There was an error while creating the template' })
        }
    }
}
"""
        with open(file_path, 'w') as file:
            file.write(content)
        print(f"Created file: {file_path}")

# Function to process template files and replace placeholders


# Process templates with both DynamoDB and Cognito configs


def process_templates(template_files, base_dir, service_name, runtime, dynamodb_config=None, cognito_config=None):
    for template_name, template_path in template_files.items():
        output_file = template_name.replace(
            '-template', '').replace('swagger', f"{service_name.strip()}-swagger")
        subfolder = "docs" if any(x in template_name for x in [
            "swagger", "hooks", "dredd"]) else ""
        output_path = os.path.join(base_dir, subfolder, output_file)

        try:
            with open(template_path, 'r') as template_file:
                content = template_file.read()

                if "serverless" in template_name and template_name.endswith(".yml"):
                    serverless_config_yml = yaml.safe_load(content)
                    serverless_config_yml["service"] = service_name.strip(
                    )
                    serverless_config_yml["provider"]["runtime"] = runtime

                    # Initialize resources if not present
                    if "resources" not in serverless_config_yml:
                        serverless_config_yml["resources"] = {
                            "Resources": {}}

                    # Add DynamoDB resources if configured
                    if dynamodb_config:
                        serverless_config_yml["resources"]["Resources"].update(
                            dynamodb_config)

                    # Add Cognito resources if configured
                    if cognito_config:
                        serverless_config_yml["resources"]["Resources"].update(
                            cognito_config)

                        # # Add Cognito environment variables
                        # if "environment" not in serverless_config_yml["provider"]:
                        #     serverless_config_yml["provider"]["environment"] = {
                        #     }

                        # serverless_config_yml["provider"]["environment"].update({
                        #     "USER_POOL_ID": {"Ref": f"{pool_name}UserPool"},
                        #     "USER_POOL_CLIENT_ID": {"Ref": f"{pool_name}UserPoolClient"},
                        #     "IDENTITY_POOL_ID": {"Ref": f"{pool_name}IdentityPool"}
                        # })

                    # Save updated YAML
                    with open(output_path, 'w') as file:
                        yaml.dump(serverless_config_yml, file,
                                    default_flow_style=False, sort_keys=False)
                else:
                    # For other files, use string replacement
                    content = content.replace(
                        "service_name", service_name.strip())
                    if "serverless" in template_name:
                        content = content.replace("run_time", runtime)

                    with open(output_path, 'w') as file:
                        file.write(content)

            print(f"Created file: {output_path}")
        except FileNotFoundError:
            print(f"Template file not found: {template_path}")


# Function to create the .env file


def create_env_file(base_dir):
    env_file_path = f"{base_dir}/.env"
    with open(env_file_path, 'w') as file:
        file.write("""STAGE=dev
DEBUG=true""")
    print(f"Created file: {env_file_path}")

# Function to check and update serverless-compose.yml


def update_serverless_compose(service_name):
    os.chdir("..")
    current_path = os.getcwd()

    compose_file = f'{current_path}/serverless-compose.yml'

    print(f"Updating existing {compose_file}...")
    with open(compose_file, 'r') as file:
        compose_data = yaml.safe_load(file) or {}

    # Ensure 'services' is initialized as a dictionary
        if 'services' not in compose_data or compose_data['services'] is None:
            compose_data['services'] = {}

    # Add new service to the services section
    service_path = f"services/{service_name.strip()}"
    compose_data['services'][service_name.strip()] = {
        'path': service_path,
        'config': "serverless.yml"
    }

    # Write updated data back to the file
    with open(compose_file, 'w') as file:
        yaml.dump(compose_data, file, default_flow_style=False)

    print(f"Service {service_name} added to {compose_file}")


def create_service_structure():
    try:
        # get current path
        current_path = os.getcwd()
        if not current_path.endswith('services'):
            print("Please navigate to the 'services' folder and try again.")
            return

        # Get the directory where the generator.py script is located
        base_package_path = importlib.resources.files(
            'folder_structure_generator_7edge')

        # Paths to template files inside the package
        template_files = {
            "dredd-template.yml": base_package_path / "dredd-template.yml",
            "serverless-template.yml": base_package_path / "serverless-template.yml",
            "hooks-template.py": base_package_path / "hooks-template.py",
            "swagger-template.json": base_package_path / "swagger-template.json",
        }

        # Prompt user for the service name
        service_name = inquirer.text(
            message="Enter the service name:").execute()
        if not service_name.strip():
            print("Error: Service name cannot be empty.")
            return

        # Ask if the user wants to add DynamoDB
        use_dynamodb = inquirer.confirm(
            message="Do you want to add a DynamoDB table?").execute()

        dynamodb_config = None
        if use_dynamodb:
            # DynamoDB table configuration
            table_name = inquirer.text(
                message="Enter the DynamoDB table name:").execute()
            if not table_name.strip():
                print("Error: table name cannot be empty.")
                return

            # Partition key prompt
            partition_key = inquirer.text(
                message="Enter the partition key for DynamoDB table:",
                default="partition_key"
            ).execute()
            if not partition_key.strip():
                print("Error: partition_key cannot be empty.")
                return

            # Sort key prompt with string default
            sort_key = inquirer.text(
                message="Enter the sort key:",
                default="sort_key"
            ).execute()
            if not sort_key.strip():
                print("Error: sort_key cannot be empty.")
                return

            # LSI configuration
            lsi_keys = []
            lsi_count = int(inquirer.number(
                message="How many local secondary indexes (LSIs) do you want to add?",
                default=0
            ).execute())

            for i in range(lsi_count):
                lsi_name = inquirer.text(
                    message=f"Enter the name of LSI #{i + 1}:"
                ).execute()
                if not lsi_name.strip():
                    print("Error: LSI name cannot be empty.")
                    return

                lsi_sort_key = inquirer.text(
                    message=f"Enter the sort key for LSI #{i + 1}:",
                    default=f"lsi_{i+1}_sort_key"
                ).execute()
                if not lsi_sort_key.strip():
                    print("Error: LSI sort key cannot be empty.")
                    return

                lsi_keys.append((lsi_name, lsi_sort_key))

            # Create DynamoDB configuration
            dynamodb_config = create_dynamodb_table_configuration(
                table_name, partition_key, sort_key, lsi_keys)

            # Ask if the user wants to add Cognito
        use_cognito = inquirer.confirm(
            message="Do you want to add a Cognito User Pool?").execute()

        cognito_config = None
        if use_cognito:
            # Cognito configuration
            pool_name = inquirer.text(
                message="Enter the Cognito User Pool name:",
                default=f"{service_name}-users"
            ).execute()
            if not pool_name.strip():
                print("Error: Pool name cannot be empty.")
                return

            client_name = inquirer.text(
                message="Enter the Cognito Client name:",
                default=f"{pool_name}-client"
            ).execute()
            if not client_name.strip():
                print("Error: Client name cannot be empty.")
                return

            # Create Cognito configuration
            cognito_config = create_cognito_user_pool_configuration(
                pool_name, client_name)

        # Language selection
        language_choice = inquirer.select(
            message="Select the programming language:",
            choices=["Python", "Node.js"]
        ).execute()

        # Determine file extension and runtime
        file_extension = "py" if language_choice == "Python" else "js"
        runtime = 'python3.11' if language_choice == 'Python' else 'nodejs14.x'

        base_path = f"{current_path}/{service_name.strip()}"

        # Create folder structure
        folders = [
            f"{base_path}/handlers",
            f"{base_path}/docs"
        ]
        create_directories(folders)

        # Create handler files
        handler_files = ["add", "list", "view", "update", "delete"]
        create_handler_files(base_path, handler_files,
                             language_choice, file_extension)

        # Process templates
               # Call process_templates with both configs
        process_templates(template_files, base_path, service_name, runtime, 
                        dynamodb_config=dynamodb_config, 
                        cognito_config=cognito_config)


        # Create .env file
        create_env_file(base_path)

        # Update serverless-compose.yml
        update_serverless_compose(service_name)

        print("\nService structure generated successfully!")

    except Exception as e:
        print(f"An error occurred: {e}")
