#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* stset.c */
/* Fortran interface file */

/*
* This file was generated automatically by bfort from the C source
* file.  
 */

#ifdef PETSC_USE_POINTER_CONVERSION
#if defined(__cplusplus)
extern "C" { 
#endif 
extern void *PetscToPointer(void*);
extern int PetscFromPointer(void *);
extern void PetscRmPointer(void*);
#if defined(__cplusplus)
} 
#endif 

#else

#define PetscToPointer(a) (a ? *(PetscFortranAddr *)(a) : 0)
#define PetscFromPointer(a) (PetscFortranAddr)(a)
#define PetscRmPointer(a)
#endif

#include "slepcst.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsettype_ STSETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsettype_ stsettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgettype_ STGETTYPE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgettype_ stgettype
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetfromoptions_ STSETFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetfromoptions_ stsetfromoptions
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetmatstructure_ STSETMATSTRUCTURE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetmatstructure_ stsetmatstructure
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetmatstructure_ STGETMATSTRUCTURE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetmatstructure_ stgetmatstructure
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetmatmode_ STSETMATMODE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetmatmode_ stsetmatmode
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetmatmode_ STGETMATMODE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetmatmode_ stgetmatmode
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsettransform_ STSETTRANSFORM
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsettransform_ stsettransform
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgettransform_ STGETTRANSFORM
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgettransform_ stgettransform
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetstructured_ STSETSTRUCTURED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetstructured_ stsetstructured
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetstructured_ STGETSTRUCTURED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetstructured_ stgetstructured
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  stsettype_(ST st,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(st);
/* insert Fortran-to-C conversion for type */
  FIXCHAR(type,cl0,_cltmp0);
*ierr = STSetType(
	(ST)PetscToPointer((st) ),_cltmp0);
  FREECHAR(type,_cltmp0);
}
SLEPC_EXTERN void  stgettype_(ST st,char *type, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(st);
*ierr = STGetType(
	(ST)PetscToPointer((st) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for type */
*ierr = PetscStrncpy(type, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, type, cl0);
}
SLEPC_EXTERN void  stsetfromoptions_(ST st, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetFromOptions(
	(ST)PetscToPointer((st) ));
}
SLEPC_EXTERN void  stsetmatstructure_(ST st,MatStructure *str, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetMatStructure(
	(ST)PetscToPointer((st) ),*str);
}
SLEPC_EXTERN void  stgetmatstructure_(ST st,MatStructure *str, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STGetMatStructure(
	(ST)PetscToPointer((st) ),str);
}
SLEPC_EXTERN void  stsetmatmode_(ST st,STMatMode *mode, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetMatMode(
	(ST)PetscToPointer((st) ),*mode);
}
SLEPC_EXTERN void  stgetmatmode_(ST st,STMatMode *mode, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STGetMatMode(
	(ST)PetscToPointer((st) ),mode);
}
SLEPC_EXTERN void  stsettransform_(ST st,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetTransform(
	(ST)PetscToPointer((st) ),*flg);
}
SLEPC_EXTERN void  stgettransform_(ST st,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STGetTransform(
	(ST)PetscToPointer((st) ),flg);
}
SLEPC_EXTERN void  stsetstructured_(ST st,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetStructured(
	(ST)PetscToPointer((st) ),*flg);
}
SLEPC_EXTERN void  stgetstructured_(ST st,PetscBool *flg, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STGetStructured(
	(ST)PetscToPointer((st) ),flg);
}
#if defined(__cplusplus)
}
#endif
