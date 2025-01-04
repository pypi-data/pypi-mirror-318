#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* matstruct.c */
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

#include "slepcsys.h"
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define matcreatebse_ MATCREATEBSE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define matcreatebse_ matcreatebse
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  matcreatebse_(Mat R,Mat C,Mat *H, int *ierr)
{
CHKFORTRANNULLOBJECT(R);
CHKFORTRANNULLOBJECT(C);
PetscBool H_null = !*(void**) H ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(H);
*ierr = MatCreateBSE(
	(Mat)PetscToPointer((R) ),
	(Mat)PetscToPointer((C) ),H);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! H_null && !*(void**) H) * (void **) H = (void *)-2;
}
#if defined(__cplusplus)
}
#endif
