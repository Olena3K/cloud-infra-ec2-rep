output "cluster_name" {
  value = aws_ecs_cluster.main.name
}

output "asg_name" {
  value = aws_autoscaling_group.ecs_asg.name
}

output "task_definition_arn" {
  value = aws_ecs_task_definition.app.arn
}

output "service_name" {
  value = aws_ecs_service.app.name
}
