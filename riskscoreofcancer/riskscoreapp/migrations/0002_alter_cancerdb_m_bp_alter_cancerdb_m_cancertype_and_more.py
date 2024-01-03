# Generated by Django 5.0 on 2023-12-23 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('riskscoreapp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cancerdb',
            name='m_BP',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_CancerType',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_ChemoTolerance',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Chemoagent',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Cycle',
            field=models.IntegerField(),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_DiabetesCI',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_DistanceFH',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Dosingagent',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Drug',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_DuringChemo',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_ECOG',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Gender',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Gradeg',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_HeartDiseaseCI',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_MentalState',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_PriorHospitalization',
            field=models.CharField(max_length=30),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Setting',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_SocialSupport',
            field=models.CharField(max_length=20),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_StageBurden',
            field=models.CharField(max_length=25),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Substanceabuse',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='cancerdb',
            name='m_Walking',
            field=models.CharField(max_length=25),
        ),
    ]