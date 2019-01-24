from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, UserManager, AbstractBaseUser,
    PermissionsMixin, Group)

STATUSES = (
    ('1', '재학생'),
    ('2', '군휴학'),
    ('3', '휴학생'),
    ('4', '졸업생'),
)

SEMESTERS = (
    ('0', '신입생'),
    ('1', '1학년 1학기'),
    ('2', '1학년 2학기'),
    ('3', '2학년 1학기'),
    ('4', '2학년 2학기'),
    ('5', '3학년 1학기'),
    ('6', '3학년 2학기'),
    ('7', '4학년 1학기'),
    ('8', '4학년 2학기'),
    ('9', '초과학기')
)

MAJORS = (
    ('01', '컴퓨터공학과'),
    ('02', '산업공학과'),
    ('03', '전기전자공학부'),
    ('04', '법학부'),
    ('05', '자율전공학부'),
    ('99', '없음')
)

# 커스텀 유저를 다루기 위한 UserManager 클래스를 재정의
class HiarcUserManager(BaseUserManager):

    use_in_migrations = True

    def create_user(self, email, username, password=None, **extra_fields):
        if not email:
            raise ValueError('Users must have an email address')
        
        user = self.model(
            email=HiarcUserManager.normalize_email(email),            
            username=username)          
        
        user.is_paid = False
        user.is_active = False
        user.is_staff = False
        user.set_password(password)

        user.real_name = extra_fields["real_name"]
        user.student_id = extra_fields["student_id"]
        user.phone_number = extra_fields["phone_number"]
        user.status = extra_fields["status"]
        user.semester = extra_fields["semester"]
        user.major = extra_fields["major"]
        user.minor = extra_fields["minor"]
        user.motivation = extra_fields["motivation"]
        user.portfolio = extra_fields["portfolio"]
        user.comment = extra_fields["comment"]
        user.codeforces_id = extra_fields["codeforces_id"]
        user.boj_id = extra_fields["boj_id"]
        user.github_id = extra_fields["github_id"]
        user.blog_url = extra_fields["blog_url"]  
        
        user.save(using=self._db)
        

        return user

    def create_superuser(self, email, username, password):
        u = self.create_user(email=email,
                            username=username,
                            password=password
                            )
        u.is_staff = True
        u.is_active = True
        u.save(using=self._db)
        return u


class HiarcUser(AbstractBaseUser,  PermissionsMixin):
    """
    # HiarcUser Model
    HI-ARC 회원이 가지는 정보들을 저장한다.

    ## 학회 가입에 필요한 정보
    * email        : 학회 가입신청할때 쓰는 이메일
    * real_name    : 학회 회원의 이름 
    * student_id   : 학회 회원의 학번을 나타낸다.
    * phone_number : 학회 회원의 전화번호를 나타낸다.
    * status       : 학회 회원의 재학 여부를 나타낸다.
    * semester     : 학회 회원이 마지막으로 수료한 학기를 나타낸다.
    * major        : 학회 회원의 주전공을 나타낸다.
    * minor        : 학회 회원의 복수전공/부전공을 나타낸다.
    
    ## 학회원 개개인의 배경을 알기 위한 정보

    * motivation : 학회에 가입을 신청하게 된 동기 
    * portfolio  : 학회에 가입하기 전에 했던 활동을 기입 
    * comment    : 학회에 하고 싶은 말

    ## 학회원의 활동을 알 수 있는 외부 서비스 관련 정보
    * codeforces_id
    * boj_id
    * topcoder_id
    * github_id  
    * blog_url   

    ## 학회 포탈을 이용할 때 필요한 정보
    * is_paid    : 회비를 납부했는가? (졸업생 제외)
    * is_active  : 학회의 시스템에 접근할 권한이 있는지 여부를 나타낸다.
    * is_staff   : 학회의 운영진인지를 나타낸다.
    * username   : 학회 포탈에서 사용할 ID

    """
    email = models.EmailField(
        verbose_name='email',
        max_length=255,
        unique=True,
    )

    real_name = models.CharField(
        verbose_name='real_name',
        max_length=20,
        blank=False
    )

    student_id = models.CharField(
        verbose_name='student_id',
        max_length=8,
        default='B000000',
        blank=False
    ) 

    phone_number = models.CharField(
        verbose_name='phone_number',
        max_length=20,
        blank=False
    )    

    status = models.CharField(
        verbose_name='status',
        max_length=1,
        choices=STATUSES,
        default='1'
    )

    semester = models.CharField(
        verbose_name='semester',
        max_length=1,
        choices=SEMESTERS,
        default='1'
    )

    major = models.CharField(
        verbose_name='major',
        choices=MAJORS,
        max_length=2,
        default='01'
    )

    minor   = models.CharField(
        verbose_name='minor',
        choices=MAJORS,
        max_length=2,
        default='99'
    )

    motivation = models.TextField(
        verbose_name='motivation',
        blank=False
    )

    portfolio = models.TextField( 
        verbose_name='portfolio'
    )

    comment = models.TextField(
        verbose_name ='comment'
    )

    codeforces_id = models.CharField(verbose_name='codeforces_id', max_length=20, blank=True)

    boj_id = models.CharField(verbose_name='boj_id', max_length=20, blank=True)

    topcoder_id = models.CharField(verbose_name='topcoder_id', max_length=20, blank=True)
    
    github_id = models.CharField(verbose_name='github_id', max_length=20, blank=True)

    blog_url = models.CharField(verbose_name='blog_url', max_length=20, blank=True)

    is_paid   = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_staff  = models.BooleanField(default=False)

    username = models.CharField(
        verbose_name='username', 
        max_length=20, 
        blank=False, 
        unique=True
    )

    objects = HiarcUserManager()

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']

    class Meta:
        app_label = 'hiarc_registration'
        db_table = "hiarc_user"
        default_permissions = ()

        """
        Database에서의 검색속도 향상을 위해 인덱스를 적용할 칼럼
        * 학번으로 빠르게 검색이 가능해야 한다.
        * email로 검색해도 빠르게 검색이 가능해야 한다.
        * 학회 포탈 ID로 검색해도 빠르게 검색이 가능해야 한다.
        """
        indexes = [
            models.Index(fields=['student_id',]), 
            models.Index(fields=['email',]),
            models.Index(fields=['username',]),
        ]

    def get_full_name(self):
        # The user is identified by their username
        return self.username

    def get_short_name(self):
        # The user is identified by their username
        return self.username

    def __str__(self):
        return self.username

    def has_perm(self, perm, obj=None):
        "Does the user have a specific permission?"
        # Simplest possible answer: Yes, always
        return self.is_admin

    def has_module_perms(self, app_label):
        "Does the user have permissions to view the app `app_label`?"
        # Simplest possible answer: Yes, always
        return True

    @property
    def is_admin(self):
        return self.is_staff