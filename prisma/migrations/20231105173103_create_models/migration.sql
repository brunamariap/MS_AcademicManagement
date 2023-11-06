-- CreateTable
CREATE TABLE "Course" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "byname" TEXT NOT NULL,
    "periodsQuantity" INTEGER NOT NULL,
    "degree" TEXT NOT NULL
);

-- CreateTable
CREATE TABLE "Discipline" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "name" TEXT NOT NULL,
    "referencePeriod" INTEGER NOT NULL,
    "code" TEXT NOT NULL,
    "isOptative" BOOLEAN NOT NULL,
    "courseId" TEXT NOT NULL,
    CONSTRAINT "Discipline_courseId_fkey" FOREIGN KEY ("courseId") REFERENCES "Course" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "SchoolClass" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "referencePeriod" INTEGER NOT NULL,
    "shift" TEXT NOT NULL,
    "courseId" TEXT NOT NULL,
    CONSTRAINT "SchoolClass_courseId_fkey" FOREIGN KEY ("courseId") REFERENCES "Course" ("id") ON DELETE CASCADE ON UPDATE CASCADE
);

-- CreateTable
CREATE TABLE "Event" (
    "id" TEXT NOT NULL PRIMARY KEY,
    "title" TEXT NOT NULL,
    "description" TEXT NOT NULL,
    "startTime" DATETIME NOT NULL,
    "endTime" DATETIME NOT NULL,
    "createdBy" TEXT NOT NULL
);
