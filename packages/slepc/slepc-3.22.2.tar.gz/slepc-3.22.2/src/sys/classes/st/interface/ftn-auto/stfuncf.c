#include "petscsys.h"
#include "petscfix.h"
#include "petsc/private/fortranimpl.h"
/* stfunc.c */
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
#define streset_ STRESET
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define streset_ streset
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stdestroy_ STDESTROY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stdestroy_ stdestroy
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stcreate_ STCREATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stcreate_ stcreate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetmatrices_ STSETMATRICES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetmatrices_ stsetmatrices
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetmatrix_ STGETMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetmatrix_ stgetmatrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetmatrixtransformed_ STGETMATRIXTRANSFORMED
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetmatrixtransformed_ stgetmatrixtransformed
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetnummatrices_ STGETNUMMATRICES
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetnummatrices_ stgetnummatrices
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stresetmatrixstate_ STRESETMATRIXSTATE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stresetmatrixstate_ stresetmatrixstate
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetpreconditionermat_ STSETPRECONDITIONERMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetpreconditionermat_ stsetpreconditionermat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetpreconditionermat_ STGETPRECONDITIONERMAT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetpreconditionermat_ stgetpreconditionermat
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetsplitpreconditioner_ STSETSPLITPRECONDITIONER
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetsplitpreconditioner_ stsetsplitpreconditioner
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetsplitpreconditionerterm_ STGETSPLITPRECONDITIONERTERM
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetsplitpreconditionerterm_ stgetsplitpreconditionerterm
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetsplitpreconditionerinfo_ STGETSPLITPRECONDITIONERINFO
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetsplitpreconditionerinfo_ stgetsplitpreconditionerinfo
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetshift_ STSETSHIFT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetshift_ stsetshift
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetshift_ STGETSHIFT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetshift_ stgetshift
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetdefaultshift_ STSETDEFAULTSHIFT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetdefaultshift_ stsetdefaultshift
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stscaleshift_ STSCALESHIFT
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stscaleshift_ stscaleshift
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetbalancematrix_ STSETBALANCEMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetbalancematrix_ stsetbalancematrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetbalancematrix_ STGETBALANCEMATRIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetbalancematrix_ stgetbalancematrix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stmatcreatevecs_ STMATCREATEVECS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stmatcreatevecs_ stmatcreatevecs
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stmatcreatevecsempty_ STMATCREATEVECSEMPTY
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stmatcreatevecsempty_ stmatcreatevecsempty
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stmatgetsize_ STMATGETSIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stmatgetsize_ stmatgetsize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stmatgetlocalsize_ STMATGETLOCALSIZE
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stmatgetlocalsize_ stmatgetlocalsize
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stsetoptionsprefix_ STSETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stsetoptionsprefix_ stsetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stappendoptionsprefix_ STAPPENDOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stappendoptionsprefix_ stappendoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stgetoptionsprefix_ STGETOPTIONSPREFIX
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stgetoptionsprefix_ stgetoptionsprefix
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stview_ STVIEW
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stview_ stview
#endif
#ifdef PETSC_HAVE_FORTRAN_CAPS
#define stviewfromoptions_ STVIEWFROMOPTIONS
#elif !defined(PETSC_HAVE_FORTRAN_UNDERSCORE) && !defined(FORTRANDOUBLEUNDERSCORE)
#define stviewfromoptions_ stviewfromoptions
#endif
/* Provide declarations for malloc/free if needed for strings */
#include <stdlib.h>


/* Definitions of Fortran Wrapper routines */
#if defined(__cplusplus)
extern "C" {
#endif
SLEPC_EXTERN void  streset_(ST st, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STReset(
	(ST)PetscToPointer((st) ));
}
SLEPC_EXTERN void  stdestroy_(ST *st, int *ierr)
{
PETSC_FORTRAN_OBJECT_F_DESTROYED_TO_C_NULL(st);
 PetscBool st_null = !*(void**) st ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(st);
*ierr = STDestroy(st);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! st_null && !*(void**) st) * (void **) st = (void *)-2;
if (*ierr) return;
PETSC_FORTRAN_OBJECT_C_NULL_TO_F_DESTROYED(st);
 }
SLEPC_EXTERN void  stcreate_(MPI_Fint * comm,ST *newst, int *ierr)
{
PETSC_FORTRAN_OBJECT_CREATE(newst);
 PetscBool newst_null = !*(void**) newst ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(newst);
*ierr = STCreate(
	MPI_Comm_f2c(*(comm)),newst);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! newst_null && !*(void**) newst) * (void **) newst = (void *)-2;
}
SLEPC_EXTERN void  stsetmatrices_(ST st,PetscInt *n,Mat A[], int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = STSetMatrices(
	(ST)PetscToPointer((st) ),*n,A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  stgetmatrix_(ST st,PetscInt *k,Mat *A, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool A_null = !*(void**) A ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(A);
*ierr = STGetMatrix(
	(ST)PetscToPointer((st) ),*k,A);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! A_null && !*(void**) A) * (void **) A = (void *)-2;
}
SLEPC_EXTERN void  stgetmatrixtransformed_(ST st,PetscInt *k,Mat *T, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool T_null = !*(void**) T ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(T);
*ierr = STGetMatrixTransformed(
	(ST)PetscToPointer((st) ),*k,T);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! T_null && !*(void**) T) * (void **) T = (void *)-2;
}
SLEPC_EXTERN void  stgetnummatrices_(ST st,PetscInt *n, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLINTEGER(n);
*ierr = STGetNumMatrices(
	(ST)PetscToPointer((st) ),n);
}
SLEPC_EXTERN void  stresetmatrixstate_(ST st, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STResetMatrixState(
	(ST)PetscToPointer((st) ));
}
SLEPC_EXTERN void  stsetpreconditionermat_(ST st,Mat mat, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(mat);
*ierr = STSetPreconditionerMat(
	(ST)PetscToPointer((st) ),
	(Mat)PetscToPointer((mat) ));
}
SLEPC_EXTERN void  stgetpreconditionermat_(ST st,Mat *mat, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool mat_null = !*(void**) mat ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(mat);
*ierr = STGetPreconditionerMat(
	(ST)PetscToPointer((st) ),mat);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! mat_null && !*(void**) mat) * (void **) mat = (void *)-2;
}
SLEPC_EXTERN void  stsetsplitpreconditioner_(ST st,PetscInt *n,Mat Psplit[],MatStructure *strp, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool Psplit_null = !*(void**) Psplit ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(Psplit);
*ierr = STSetSplitPreconditioner(
	(ST)PetscToPointer((st) ),*n,Psplit,*strp);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! Psplit_null && !*(void**) Psplit) * (void **) Psplit = (void *)-2;
}
SLEPC_EXTERN void  stgetsplitpreconditionerterm_(ST st,PetscInt *k,Mat *Psplit, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool Psplit_null = !*(void**) Psplit ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(Psplit);
*ierr = STGetSplitPreconditionerTerm(
	(ST)PetscToPointer((st) ),*k,Psplit);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! Psplit_null && !*(void**) Psplit) * (void **) Psplit = (void *)-2;
}
SLEPC_EXTERN void  stgetsplitpreconditionerinfo_(ST st,PetscInt *n,MatStructure *strp, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLINTEGER(n);
*ierr = STGetSplitPreconditionerInfo(
	(ST)PetscToPointer((st) ),n,strp);
}
SLEPC_EXTERN void  stsetshift_(ST st,PetscScalar *shift, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetShift(
	(ST)PetscToPointer((st) ),*shift);
}
SLEPC_EXTERN void  stgetshift_(ST st,PetscScalar* shift, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLSCALAR(shift);
*ierr = STGetShift(
	(ST)PetscToPointer((st) ),shift);
}
SLEPC_EXTERN void  stsetdefaultshift_(ST st,PetscScalar *defaultshift, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STSetDefaultShift(
	(ST)PetscToPointer((st) ),*defaultshift);
}
SLEPC_EXTERN void  stscaleshift_(ST st,PetscScalar *factor, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
*ierr = STScaleShift(
	(ST)PetscToPointer((st) ),*factor);
}
SLEPC_EXTERN void  stsetbalancematrix_(ST st,Vec D, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(D);
*ierr = STSetBalanceMatrix(
	(ST)PetscToPointer((st) ),
	(Vec)PetscToPointer((D) ));
}
SLEPC_EXTERN void  stgetbalancematrix_(ST st,Vec *D, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool D_null = !*(void**) D ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(D);
*ierr = STGetBalanceMatrix(
	(ST)PetscToPointer((st) ),D);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! D_null && !*(void**) D) * (void **) D = (void *)-2;
}
SLEPC_EXTERN void  stmatcreatevecs_(ST st,Vec *right,Vec *left, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool right_null = !*(void**) right ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(right);
PetscBool left_null = !*(void**) left ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(left);
*ierr = STMatCreateVecs(
	(ST)PetscToPointer((st) ),right,left);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! right_null && !*(void**) right) * (void **) right = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! left_null && !*(void**) left) * (void **) left = (void *)-2;
}
SLEPC_EXTERN void  stmatcreatevecsempty_(ST st,Vec *right,Vec *left, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
PetscBool right_null = !*(void**) right ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(right);
PetscBool left_null = !*(void**) left ? PETSC_TRUE : PETSC_FALSE;
CHKFORTRANNULLOBJECT(left);
*ierr = STMatCreateVecsEmpty(
	(ST)PetscToPointer((st) ),right,left);
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! right_null && !*(void**) right) * (void **) right = (void *)-2;
// if C routine nullifed the object, we must set to to -2 to indicate null set in Fortran
if (! left_null && !*(void**) left) * (void **) left = (void *)-2;
}
SLEPC_EXTERN void  stmatgetsize_(ST st,PetscInt *m,PetscInt *n, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLINTEGER(m);
CHKFORTRANNULLINTEGER(n);
*ierr = STMatGetSize(
	(ST)PetscToPointer((st) ),m,n);
}
SLEPC_EXTERN void  stmatgetlocalsize_(ST st,PetscInt *m,PetscInt *n, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLINTEGER(m);
CHKFORTRANNULLINTEGER(n);
*ierr = STMatGetLocalSize(
	(ST)PetscToPointer((st) ),m,n);
}
SLEPC_EXTERN void  stsetoptionsprefix_(ST st, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(st);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = STSetOptionsPrefix(
	(ST)PetscToPointer((st) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  stappendoptionsprefix_(ST st, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(st);
/* insert Fortran-to-C conversion for prefix */
  FIXCHAR(prefix,cl0,_cltmp0);
*ierr = STAppendOptionsPrefix(
	(ST)PetscToPointer((st) ),_cltmp0);
  FREECHAR(prefix,_cltmp0);
}
SLEPC_EXTERN void  stgetoptionsprefix_(ST st, char *prefix, int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(st);
*ierr = STGetOptionsPrefix(
	(ST)PetscToPointer((st) ),(const char **)&_cltmp0);
/* insert C-to-Fortran conversion for prefix */
*ierr = PetscStrncpy(prefix, _cltmp0, cl0);
                        if (*ierr) return;
                        FIXRETURNCHAR(PETSC_TRUE, prefix, cl0);
}
SLEPC_EXTERN void  stview_(ST st,PetscViewer viewer, int *ierr)
{
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(viewer);
*ierr = STView(
	(ST)PetscToPointer((st) ),PetscPatchDefaultViewers((PetscViewer*)viewer));
}
SLEPC_EXTERN void  stviewfromoptions_(ST st,PetscObject obj, char name[], int *ierr, PETSC_FORTRAN_CHARLEN_T cl0)
{
  char *_cltmp0 = PETSC_NULLPTR;
CHKFORTRANNULLOBJECT(st);
CHKFORTRANNULLOBJECT(obj);
/* insert Fortran-to-C conversion for name */
  FIXCHAR(name,cl0,_cltmp0);
*ierr = STViewFromOptions(
	(ST)PetscToPointer((st) ),
	(PetscObject)PetscToPointer((obj) ),_cltmp0);
  FREECHAR(name,_cltmp0);
}
#if defined(__cplusplus)
}
#endif
