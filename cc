public class MySampleApexClass {
public Double myValue = 0; 
public Double get() {

myValue = myValue+10;
return myValue;
}
}

MySampleApexClass m=new MySampleApexClass();
Double Value=m.get();
system.debug('valued='+Value);

public class StudentController {


public static void addStudent(String name, Integer age, String email, String course) {
Student__c s = new Student__c();

s.Name = name;
s.Age__c = age;
s.Email__c = email;
s.Course__c = course;
insert s;
}

// Method to get all students
public static List<Student__c> getStudents() {
return [SELECT Id, Name, Age__c, Email__c, Course__c FROM Student__c];
}
}

StudentController.addStudent('Rahul Sharma', 20, 'rahul@email.com', 'Computer Engineering');
