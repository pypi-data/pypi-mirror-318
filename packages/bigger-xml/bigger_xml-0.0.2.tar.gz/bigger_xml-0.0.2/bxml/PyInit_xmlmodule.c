/*
 * MIT License
 * Copyright (c) 2025 Bhautik Sudani
 *
 * Permission is hereby granted, free of charge, to any person obtaining a copy
 * of this software and associated documentation files (the "Software"), to deal
 * in the Software without restriction, including without limitation the rights
 * to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
 * copies of the Software, and to permit persons to whom the Software is
 * furnished to do so, subject to the following conditions:
 *
 * The above copyright notice and this permission notice shall be included in all
 * copies or substantial portions of the Software.
 *
 * THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
 * IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
 * FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
 * AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
 * LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
 * OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
 * SOFTWARE.
 */

#include <Python.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>


const char *XML_STARTTAG_STARTING = "<";
const char *XML_ENDTAG_STARTING = "</";
const char *XML_TAG_ENDING = ">";
const char *XML_SELFCLOSING_TAG = " />";

typedef struct {
    char* key;
    char* val;
    struct Attribute* next;
} Attribute;

typedef struct {
    char* tag;
    char* text;
    struct Element* next;
    struct Element* previous;
    struct Element* startChild;
    struct Element* parent;
    struct Element* endChild;
    struct Attribute* attr;
} Element;

#define CAPSULE_NAME "Element"

// Create One Key Value Pair For Any XML Tag
struct Attribute* CreateKey(char* key, char* val){
    Attribute *new_attr = (Attribute*)malloc(sizeof(Attribute));
    new_attr->key = strdup(key);
    new_attr->val = strdup(val);
    new_attr->next = NULL;
    return new_attr;
}

// Create XML Tag
Element* CreateElement(char* tag){
    Element* e = (Element*)malloc(sizeof(Element));
    if(e == NULL){
        return NULL;
    }
    e->tag = strdup(tag);
    e->text = NULL;
    e->startChild = NULL;
    e->parent = NULL;
    e->endChild = NULL;
    e->next = NULL;
    e->previous = NULL;
    e->attr = NULL;
    return e;
}

// Release Memory Occuiped to store XML Tag & Attributes
static void FreeMemory(Element* root){
    Element* temp = root;
    while(root){
        // printf("Cleaning Memory\n");
        if(root->startChild != NULL){
            // printf("Calling Child\n");
            FreeMemory(root->startChild);
        }

        Attribute* attr = root->attr;
        Attribute* temp_attr = NULL;
        while(attr) {
            free(attr->key);
            free(attr->val);
            temp_attr = attr->next;
            free(attr);
            attr = temp_attr;
        }

        if(root->tag != NULL){
            // printf("Cleaning Tag\n");
            free(root->tag);
        }
        if(root->text != NULL){
            // printf("Cleaning Text\n");
            free(root->text);
        }
        // printf("Memory Cleanup Done\n");
        temp = root->next;
        free(root);
        root = temp;
    }
}
static void freeXML(PyObject* self){
    Element *element = (Element *) PyCapsule_GetPointer(self, CAPSULE_NAME);
    FreeMemory(element);
}

// Create Base or Child XML Tag
// Create Child XML Tag
static PyObject* childElement(PyObject* self, PyObject* args) {
    PyObject* parentCapsule;
    const char* tagName;

    // Parse the input argument (capsule)
    if (!PyArg_ParseTuple(args, "Os", &parentCapsule,&tagName)) {
        return NULL;
    }

    Element* child = CreateElement(tagName);
    if(child == NULL){
        return NULL;
    }

    PyObject* childCapsule = PyCapsule_New((void*)child,CAPSULE_NAME,NULL);
    if(childCapsule == NULL){
        free(child->tag);
        free(child);
        return NULL;
    }

    Element* parent = (Element*)PyCapsule_GetPointer(parentCapsule, CAPSULE_NAME);
    if (parent == NULL) {
        return NULL;  // Return NULL if the capsule doesn't contain a valid struct
    }

    if( parent->endChild==NULL ){
        parent->startChild = child;
        parent->endChild = child;
    } else {
        Element* temp = parent->endChild;
        temp->next = child;
        child->previous = temp;
        parent->endChild = child;
    }
    child->parent = parent;

    return childCapsule;
}
// Create Base XML Tag
static PyObject* baseElement(PyObject* self, PyObject* args) {
    const char* tagName;
    if (!PyArg_ParseTuple(args, "s", &tagName)) {
        return NULL;  // Return NULL if parsing fails
    }
    
    Element* e = CreateElement(tagName);
    if(e == NULL){
        return NULL;
    }

    PyObject* capsule = PyCapsule_New((void*)e,CAPSULE_NAME,freeXML);
    if(capsule == NULL){
        free(e->tag);
        free(e);
        return NULL;
    }

    return capsule;
}

// Delete Tag

// Set Text For XML Tag
static PyObject* deleteElement(PyObject* self, PyObject* args) {
    PyObject* rootCapsule;

    // Parse the input argument (capsule)
    if (!PyArg_ParseTuple(args, "O", &rootCapsule)) {
        return NULL;
    }

    Element* root = (Element*)PyCapsule_GetPointer(rootCapsule, CAPSULE_NAME);
    Element* parent = root->parent;
    Element* pre = root->previous;
    Element* next = root->next;


    if(parent == NULL){
        Py_RETURN_NONE;
    } else {
        if(pre == NULL){
            if(next == NULL){
                parent -> startChild = NULL;
                parent -> endChild = NULL;
            } else {
                parent->startChild = next;
                root -> next = NULL;
            }
        } else {
            if(next == NULL){
                parent -> endChild = pre;
                pre -> next = NULL;
                root -> previous = NULL;
            } else {
                pre -> next = next;
                next -> previous = pre;
                root -> previous = NULL;
                root -> next = NULL;
            }
        }
    }
    FreeMemory(root);
    Py_RETURN_NONE;
}


// Add Key-Value Attribute to XML Tag
// Find And Update Value or add New Key-Value Pair at End
void SearchAndSetAttribute(Attribute* attr,char* key,char* val){
    if(strcmp(attr->key,key) == 0) {
        free(attr->val);
        attr->val = strdup(key);
    } else {
        if(attr->next == NULL){
            Attribute* new_attr = CreateKey(key,val);
            attr->next = new_attr;
        } else {
            SearchAndSetAttribute(attr->next,key,val);
        }
    }
}
// Create Key-Value Pair
void SetKey(Element* root,char* key,char* val) {
    if(root->attr == NULL){
        Attribute* attr = CreateKey(key,val);
        root->attr = attr;
    } else {
        SearchAndSetAttribute(root->attr,key,val);
    }
}
// Key Value Pair add to XML Tag
static PyObject* addKey(PyObject* self, PyObject* args) {
    PyObject* rootCapsule;
    char* key;
    char* val;

    // Parse the input argument (capsule)
    if (!PyArg_ParseTuple(args, "Oss", &rootCapsule,&key,&val)) {
        return NULL;
    }

    Element* root = (Element*) PyCapsule_GetPointer(rootCapsule, CAPSULE_NAME);

    SetKey(root,key,val);

    Py_RETURN_NONE;
}

// Find Element With Provided Tag String
// Search Recursively To Find XML Tag
void FindRec(Element* root,char* search_str,void ***ref_array,int* size){

    Element* xml = root;
    while(xml) {
        if(strcmp(xml->tag,search_str) == 0 ){
            *size+=1;
            *ref_array = realloc(*ref_array,(*size) * sizeof(void*));
            (*ref_array)[*size-1] = xml;
        }
        if(xml->startChild != NULL)
        {
            FindRec(xml->startChild,search_str,ref_array,size);
        }
        xml = xml->next;
    }
}
// Find XML Tag Matches With Provided String
static PyObject* findAll(PyObject* self, PyObject* args){
    PyObject* rootCapsule;
    const char* search;

    if (!PyArg_ParseTuple(args, "Os", &rootCapsule,&search)) {
        return NULL;
    }


    Element* root = (Element*) PyCapsule_GetPointer(rootCapsule, CAPSULE_NAME);
    int *size = malloc(sizeof(int));
    *size = 0;

    void **ref_array = NULL;
    FindRec(root,search,&ref_array,size);

    PyObject *py_list = PyList_New(*size);
    int itr = 0;
    // printf("Result Size is %d \n",*size);
    while (itr < *size)
    { 
        Element* e = (Element*)ref_array[itr];
        PyObject* py_obj = PyCapsule_New((void*)e,CAPSULE_NAME,NULL);
        // printf("Item Found");
        PyList_SetItem(py_list,itr,py_obj);
        itr++;
    }
    free(ref_array);
    return py_list;
}

// Generate XML and save as file
void GenerateXML(Attribute* attr,FILE* xmlfile){
    while(attr){
        fprintf(xmlfile," ");
        fprintf(xmlfile,attr->key);
        fprintf(xmlfile,"=\'");
        fprintf(xmlfile,attr->val);
        fprintf(xmlfile,"\'");
        attr = attr->next;
    }
}

void SaveXML(Element* root,char* tab,FILE* xmlFile){

    Element* xmlRef = root;
    while(xmlRef) {
        if(xmlRef->text != NULL || xmlRef->startChild != NULL) {
            // printf("%s<%s>",tab,root->tag); 
            fprintf(xmlFile,tab);
            fprintf(xmlFile,XML_STARTTAG_STARTING);
            fprintf(xmlFile,xmlRef->tag);
            GenerateXML(xmlRef->attr,xmlFile);
            fprintf(xmlFile,XML_TAG_ENDING);
            if(xmlRef->text != NULL){
                // printf("%s",root->text);
                fprintf(xmlFile,xmlRef->text); 
            }
            if(xmlRef->startChild != NULL){
                // printf("\n");
                fprintf(xmlFile,"\n");
                char* extraTab = (char*)malloc(strlen(tab) + strlen("  ") + 1);
                strcpy(extraTab,tab);
                strcat(extraTab,"  ");
                SaveXML(xmlRef -> startChild,extraTab,xmlFile);
                free(extraTab);
                // printf("%s",tab);
                fprintf(xmlFile,tab);
            }
            // printf("</%s>\n",root->tag); 
                fprintf(xmlFile,XML_ENDTAG_STARTING);
                fprintf(xmlFile,xmlRef->tag);
                fprintf(xmlFile,XML_TAG_ENDING);
                fprintf(xmlFile,"\n");
        } else {
                fprintf(xmlFile,tab);
                fprintf(xmlFile,XML_STARTTAG_STARTING);
                fprintf(xmlFile,xmlRef->tag);
                fprintf(xmlFile,XML_SELFCLOSING_TAG);
                fprintf(xmlFile,"\n");
            // printf("%s<%s />\n",tab,root->tag);
        }
        xmlRef = xmlRef-> next;
    }
    free(xmlRef);
}

static PyObject* generateXML(PyObject* self, PyObject* args){
    PyObject* rootCapsule;
    const char* fileName;
    const char* encoding;
    int xmlDeclaration;

    // Parse the input argument (capsule)
    if (!PyArg_ParseTuple(args, "Ossb", &rootCapsule,&fileName,&encoding,&xmlDeclaration)) {
        return NULL;
    }
    Element* root = (Element*) PyCapsule_GetPointer(rootCapsule, CAPSULE_NAME);

    char* spacingStr = (char*)malloc(1);
    strcpy(spacingStr,"");
    FILE* file = fopen(strcat(fileName,".xml"), "w");
    if (file == NULL) {
        perror("Unable to open file");
        return NULL;
    }

    if(xmlDeclaration){
        fprintf(file,"<?xml version=\'1.0\' encoding=\'");
        fprintf(file,encoding);
        fprintf(file,"\'?>\n");
    }
    SaveXML(root,spacingStr,file);
    fclose(file);
    return self;
}

// Set Text For XML Tag
static PyObject* setText(PyObject* self, PyObject* args) {
    PyObject* parentCapsule;
    char* tagText;

    // Parse the input argument (capsule)
    if (!PyArg_ParseTuple(args, "Os", &parentCapsule,&tagText)) {
        return NULL;
    }

    Element* parent = (Element*)PyCapsule_GetPointer(parentCapsule, CAPSULE_NAME);
    if (parent == NULL) {
        return NULL;  // Return NULL if the capsule doesn't contain a valid struct
    }
    parent->text = strdup(tagText);
    Py_RETURN_NONE;
}

// Define the method table
static PyMethodDef methods[] = {
    {"baseElement", baseElement, METH_VARARGS, "Create Base XML Tag"},
    {"childElement", childElement, METH_VARARGS, "Add XML tag inside as child tag to any existing XML tag"},
    {"deleteElement", deleteElement, METH_VARARGS, "Add XML tag inside as child tag to any existing XML tag"},
    {"setText", setText, METH_VARARGS, "Add text to any XML Tag"},
    {"generateXML", generateXML, METH_VARARGS, "Generate and save XML."},
    {"findAll", findAll, METH_VARARGS, "Search and fild all tags matches with search string"},
    {"addKey", addKey, METH_VARARGS, "Add key to XML tag."},
    // {"get_text", get_text, METH_VARARGS, "Set the text value of an XML element"},
    {NULL, NULL, 0, NULL}
};

// Module definition
static struct PyModuleDef xmlmodule = {
    PyModuleDef_HEAD_INIT,
    "xmlmodule",  // Module name
    "A simple XML manipulation module",  // Module docstring
    -1,  // Size of module state
    methods  // The methods
};

// Module initialization
PyMODINIT_FUNC PyInit_xmlmodule(void) {
    return PyModule_Create(&xmlmodule);
}