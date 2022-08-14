docker stop testlens_web_1
docker stop testlens_db_1
docker rm testlens_web_1
docker rm testlens_db_1
Remove-Item 'C:\Users\jonat\Documents\GitHub\TestLens\data'  -Recurse