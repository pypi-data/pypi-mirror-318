data "external" "env" {
  program = ["../../envs.sh"]
}

#AWS Provider with profile Stage account
provider "aws" {
  region = var.REGION
  alias = "deployment-eu"   # Specify a default AWS region here
  profile = "belinapayroll-${var.STAGE}"
}


resource "null_resource" "nodejs" {
  provisioner "local-exec" {
    command = "npm i --force && mkdir layer && mv node_modules layer && cd layer && mkdir nodejs && mv node_modules nodejs"
  }
}



resource "aws_lambda_layer_version" "lambda_node_layer" {
  layer_name          = "node_dependency"
  filename            = data.archive_file.node_layer_code_zip.output_path
  provider = aws.deployment-eu
}

data "archive_file" "node_layer_code_zip" {
  type        = "zip"
  source_dir  = "./layer"
  output_path = "./nodejs.zip"
  depends_on = [resource.null_resource.nodejs]
}

resource "aws_ssm_parameter" "s3_bucket" {
  name  = "COMMON_LIB_ARN"
  overwrite = true
  type  = "String"
  value = aws_lambda_layer_version.lambda_node_layer.arn
  provider = aws.deployment-eu
}