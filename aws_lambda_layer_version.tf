resource "aws_lambda_layer_version" "model" {
  compatible_runtimes = ["python3.8"]
  filename            = "animal-crossing-apigateway-model.zip"
  source_code_hash    = filebase64sha256(archive_file.model.output_path)
}