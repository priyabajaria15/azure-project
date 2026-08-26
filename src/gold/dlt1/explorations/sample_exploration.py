# Databricks notebook source
# /// script
# [tool.databricks.environment]
# environment_version = "5"
# ///
# MAGIC %sql
# MAGIC select * from spotify_cata.gold.dimuser

# COMMAND ----------

# MAGIC
# MAGIC %sql
# MAGIC
# MAGIC SELECT
# MAGIC     user_id,
# MAGIC     user_name,
# MAGIC     updated_at,
# MAGIC     `__START_AT`,
# MAGIC     `__END_AT`
# MAGIC FROM spotify_cata.gold.dimuser
# MAGIC ORDER BY user_id, `__START_AT`;