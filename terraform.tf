terraform {
  backend "s3" {
    bucket = "x"
    key    = "AnimalCrossing/ApiGatewayLambdaLayer/terraform.tfstate"
    region = "y"
  }
}
