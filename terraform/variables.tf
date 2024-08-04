variable "vpc_cidr_block" {}
variable "subnet_cidr_block" {}
variable "env_prefix" {}
variable "instance_type" {}
variable "my_ip" {}
variable "public_key_location" {}

variable "instances_count" {
  description = "Total number of instances to launch"
  type        = number
  default     = 1
}
