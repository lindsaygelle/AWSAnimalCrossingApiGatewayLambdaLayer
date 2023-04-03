data "archive_file" "model" {
  output_path = "./animal-crossing-apigateway-model.zip"
  source_dir  = "./model"
  type        = "zip"
}