# Generated by Django 4.2.4 on 2023-08-11 11:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('garagem', '0005_acessorio'),
    ]

    operations = [
        migrations.CreateModel(
            name='Veiculo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ano', models.IntegerField(max_length=100)),
                ('descricao', models.CharField(max_length=100)),
                ('preco', models.DecimalField(decimal_places=2, max_digits=5)),
                ('cor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garagem.cor')),
                ('modelo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='garagem.modelo')),
            ],
        ),
    ]